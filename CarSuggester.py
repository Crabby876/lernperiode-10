import os
import sys
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score


client = MongoClient("mongodb://localhost:27017/")

db = client["CarSuggester"]
collection = db["data"]

daten = list(collection.find())

for d in daten:
    d.pop('_id', None)

df = pd.DataFrame(daten)
df['Transmission Type'] = df['Transmission Type'].replace({'MANUAL': 1, 'AUTOMATIC': 0, 'AUTOMATED_MANUAL' : -1,'DIRECT_DRIVE': 0, 'UNKNOWN' : None})
df['Driven_Wheels'] = df['Driven_Wheels'].replace({'rear wheel drive': 1, 'front wheel drive': 0, 'all wheel drive': -1, 'four wheel drive' : -1})
df['Vehicle Style'] = df['Vehicle Style'].replace
({
    'Sedan': 'Limousine',
    'Convertible': 'Cabrio',
    'Convertible SUV': 'Cabrio',
    '2dr Hatchback': 'Combi',
    '4dr Hatchback': 'Combi',
    'Wagon': 'Combi',
    'Coupe': 'Coupe',
    '4dr SUV': 'SUV',
    '2dr SUV': 'SUV',
    'Passenger Van': 'Van',
    'Passenger Minivan': 'Van',
    'Cargo Van': 'Van',
    'Cargo Minivan': 'Van',
    'Crew Cab Pickup': 'Pickup',
    'Regular Cab Pickup': 'Pickup',
    'Extended Cab Pickup': 'Pickup'
})
df['Engine HP'] = pd.to_numeric(df['Engine HP'])
df['MarkeModell'] = df['Make'] + "_" + df['Model']


y = df['MarkeModell']


df_encoded = pd.get_dummies(df, columns=['Vehicle Style', 'Make', 'Model'])


RF = RandomForestClassifier()
X = df_encoded.drop(columns=['MarkeModell', 'city mpg', 'Popularity', 'highway MPG', 'Vehicle Size', 'Market Category', 'Engine Cylinders', 'Engine Fuel Type',])
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
RF.fit(X_train, y_train)

#y_pred = RF.predict(X_test)


#print("Genauigkeit je Spalte:")
#print("Automarke + Modell: ", accuracy_score(y_test, y_pred))

os.system('cls')

jahr = int(input("Baujahr des Autos (z.B. 2018): "))
ps = float(input("Motorleistung in PS (z.B. 150): "))
getriebe = input("Getriebeart (MANUAL, AUTOMATIC, AUTOMATED_MANUAL): ")
antrieb = input("Antriebsart (rear wheel drive, front wheel drive, all wheel drive): ")
tueren = int(input("Anzahl der Türen (z.B. 4): "))
karosserie = input("Fahrzeugstil (Limousine, Cabrio, Combi, Coupe, SUV, Van, Pickup): ")
preis = float(input("Preis in CHF (z.B. 25000): "))

getriebe_map = {'MANUAL': 1, 'AUTOMATIC': 0, 'AUTOMATED_MANUAL': -1, 'DIRECT_DRIVE': 0, 'UNKNOWN': None}
antrieb_map = {'rear wheel drive': 1, 'front wheel drive': 0, 'all wheel drive': -1, 'four wheel drive': -1}

getriebe_wert = getriebe_map.get(getriebe.upper(), None) 
antrieb_wert = antrieb_map.get(antrieb.lower(), None)
preis= preis * 1,19

neue_daten = {
    'Year': jahr,
    'Engine HP': ps,
    'Transmission Type': getriebe,
    'Driven_Wheels': antrieb,
    'Number of Doors': tueren,
    'Price': preis,
    'Vehicle Style': karosserie,
}

input_df = pd.DataFrame([neue_daten])
input_df = pd.get_dummies(input_df)

for spalte in X.columns:
    if spalte not in input_df.columns:
        input_df[spalte] = None

input_df = input_df[X.columns]
os.system('cls')
print("ein Moment...")

vorhersage = RF.predict(input_df)
os.system('cls')
print("Ich schlage dir ein ", vorhersage[0], " vor")
# Man muss Year, Engine HP, Transmission Type, Driven_Wheels, Number of Doors, Vehicle Style &  Price Angeben.