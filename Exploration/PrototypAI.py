import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder 


data = {
    'age': [25, 30, 35, 40, 45, 50],
    'cartype': ['Cabrio', 'Coupe', 'Cabrio', 'SUV', 'SUV', 'Coupe'],
    'carbrand': ['BMW', 'Mercede', 'Audi', 'Mercedes', 'Jeep', 'BMW'],
    'price': [30000, 25000, 35000, 50000, 45000, 28000],
}

df = pd.DataFrame(data)

le_cartype = LabelEncoder()
le_carbrand = LabelEncoder()

df['cartype'] = le_cartype.fit_transform(df['cartype'])
df['carbrand'] = le_carbrand.fit_transform(df['carbrand'])

X = df[['age', 'price', 'cartype']]
Y = df['carbrand']

model = DecisionTreeClassifier()
model.fit(X, Y)

cartype_input = le_cartype.transform(['Coupe'])[0]
prediction = model.predict([[30, 27000, cartype_input]])

predicted_carbrand = le_carbrand.inverse_transform(prediction)

print(f"Empfohlenes Auto: {predicted_carbrand[0]}")


