import os
import sys
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib


def daten_vorbereiten_und_trainieren(collection, modell_datei="modell_rf.pkl"):
    daten = list(collection.find())
    for d in daten:
        d.pop('_id', None)

    df = pd.DataFrame(daten)

    df['Transmission Type'] = df['Transmission Type'].replace({
        'MANUAL': 1, 'AUTOMATIC': 0, 'AUTOMATED_MANUAL': -1, 'DIRECT_DRIVE': 0, 'UNKNOWN': None})
    df['Driven_Wheels'] = df['Driven_Wheels'].replace({
        'rear wheel drive': 1, 'front wheel drive': 0, 'all wheel drive': -1, 'four wheel drive': -1})
    df['Vehicle Style'] = df['Vehicle Style'].replace({
        'Sedan': 'Limousine', 'Convertible': 'Cabrio', 'Convertible SUV': 'Cabrio',
        '2dr Hatchback': 'Combi', '4dr Hatchback': 'Combi', 'Wagon': 'Combi',
        'Coupe': 'Coupe', '4dr SUV': 'SUV', '2dr SUV': 'SUV',
        'Passenger Van': 'Van', 'Passenger Minivan': 'Van', 'Cargo Van': 'Van',
        'Cargo Minivan': 'Van', 'Crew Cab Pickup': 'Pickup', 'Regular Cab Pickup': 'Pickup',
        'Extended Cab Pickup': 'Pickup'
    })
    df['Engine HP'] = pd.to_numeric(df['Engine HP'], errors='coerce')
    df['MarkeModell'] = df['Make'] + " " + df['Model']

    y = df['MarkeModell']
    df_encoded = pd.get_dummies(df, columns=['Vehicle Style', 'Make', 'Model'])

    X = df_encoded.drop(columns=['MarkeModell', 'city mpg', 'Popularity', 'highway MPG',
                                 'Vehicle Size', 'Market Category', 'Engine Cylinders',
                                 'Engine Fuel Type'], errors='ignore')

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    RF = RandomForestClassifier()
    RF.fit(X_train, y_train)

    joblib.dump((RF, X.columns.tolist()), modell_datei)

    return RF, X.columns.tolist()


# MongoDBVerbindung
client = MongoClient("mongodb://localhost:27017/")
db = client["CarSuggester"]
collection = db["data"]
modell_datei = "modell_rf.pkl"

# Modell laden oder trainieren
if os.path.exists(modell_datei):
    RF, spalten = joblib.load(modell_datei)
else:
    print("loading...")
    RF, spalten = daten_vorbereiten_und_trainieren(collection, modell_datei)

os.system('cls' if os.name == 'nt' else 'clear')

# Usereingaben
jahr = int(input("Baujahr des Autos (z.B. 2018): "))
ps = float(input("Motorleistung in PS (z.B. 150): "))
getriebe = input("Getriebeart (MANUAL, AUTOMATIC, AUTOMATED_MANUAL): ")
antrieb = input("Antriebsart (rear wheel drive, front wheel drive, all wheel drive): ")
tueren = int(input("Anzahl der Türen (z.B. 4): "))
karosserie = input("Fahrzeugstil (Limousine, Cabrio, Combi, Coupe, SUV, Van, Pickup): ")
preis = float(input("Preis in CHF (z.B. 25000): "))

# Anpassung
getriebe_map = {'MANUAL': 1, 'AUTOMATIC': 0, 'AUTOMATED_MANUAL': -1, 'DIRECT_DRIVE': 0, 'UNKNOWN': None}
antrieb_map = {'rear wheel drive': 1, 'front wheel drive': 0, 'all wheel drive': -1, 'four wheel drive': -1}

getriebe_wert = getriebe_map.get(getriebe.upper(), None)
antrieb_wert = antrieb_map.get(antrieb.lower(), None)
preis = preis * 1.19

neue_daten = {
    'Year': jahr,
    'Engine HP': ps,
    'Transmission Type': getriebe_wert,
    'Driven_Wheels': antrieb_wert,
    'Number of Doors': tueren,
    'Price': preis,
    'Vehicle Style': karosserie,
}

# Vorbereitung für Vorhersage
input_df = pd.DataFrame([neue_daten])
input_df = pd.get_dummies(input_df)

for spalte in spalten:
    if spalte not in input_df.columns:
        input_df[spalte] = None

input_df = input_df[spalten]

# Vorhersage
os.system('cls' if os.name == 'nt' else 'clear')

vorhersage = RF.predict(input_df)
os.system('cls' if os.name == 'nt' else 'clear')
print("Ich schlage dir ein", vorhersage[0], "vor")

zufriedenheit = input("Bist du zufrieden mit der Empfehlung? [y/n] ")

if zufriedenheit.strip().lower() == "n":
    gewünschtesAuto = input("Welches Auto hättest du dir überlegt? (zB. BMW 1 Series): ")
    try:
        make, model = gewünschtesAuto.strip().split(" ", 1)
        neue_daten['Make'] = make
        neue_daten['Model'] = model
    except ValueError:
        print("Fehler: Bitte gib Marke und Modell im Format 'BMW 1 Series' an.")
        sys.exit(1)
    collection.insert_one(neue_daten)
    RF, spalten = daten_vorbereiten_und_trainieren(collection, modell_datei)
    print("Danke für den Hinweis, das merke ich mir für das nächste Mal.")

elif zufriedenheit.strip().lower() == "y":
    print("Alles klar, danke!")

else:
    print("Ungültige Eingabe.")
