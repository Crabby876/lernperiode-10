from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import accuracy_score

client = MongoClient("mongodb://localhost:27017/")

db = client["CarSuggester"]
collection = db["data"]

daten = list(collection.find())

for d in daten:
    d.pop('_id', None)

df = pd.DataFrame(daten)
df['geschlecht'] = df['geschlecht'].replace({'Männlich': 1, 'Weiblich': 0})


DT = tree.DecisionTreeClassifier()
X = df[['alter', 'preis', 'geschlecht']]
y = df[['automarke', 'modell']]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

DT.fit(X_train, y_train)

y_pred = DT.predict(X_test)

print("Genauigkeit je Spalte:")
print("Automarke:", accuracy_score(y_test['automarke'], [p[0] for p in y_pred]))
print("Modell:", accuracy_score(y_test['modell'], [p[1] for p in y_pred]))