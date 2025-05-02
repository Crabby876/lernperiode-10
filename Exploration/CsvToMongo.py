import pandas as pd
from pymongo import MongoClient


client = MongoClient("mongodb://localhost:27017/")
db = client["CarSuggester"] 
collection = db["data"] 

df = pd.read_csv(r'c:\Users\dorig\OneDrive - BBBaden\BBB\LA\LP10\erweiterter_datensatz_5000.csv', encoding='cp1252')

collection.insert_many(df.to_dict(orient='records'))