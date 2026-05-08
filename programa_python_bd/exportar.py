import pandas as pd
from pymongo import MongoClient
import matplotlib.pyplot as plt

cliente = MongoClient("mongodb+srv://2124200328_db_user:goTe8610@cluster0.hr2uuz8.mongodb.net/?appName=Cluster0")
db = cliente["iot"]
coleccion = db["humedad"]

datos = list(coleccion.find({}, {"_id": 0}))
df = pd.DataFrame(datos)
df.to_csv("humedad.csv", index=False)

df['fecha'] = pd.to_datetime(df['fecha'])
plt.style.use('dark_background')
plt.figure(figsize=(12, 6))
plt.plot(df['fecha'], df['humedad'], color='cyan', marker='o')
plt.title("Humedad del Suelo")
plt.xlabel("Fecha")
plt.ylabel("Nivel de Humedad")
plt.grid(True)
plt.tight_layout()
plt.show()