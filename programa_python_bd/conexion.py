from flask import Flask, request
from pymongo import MongoClient
from datetime import datetime

app = Flask(__name__)
cliente = MongoClient("mongodb+srv://2124200328_db_user:goTe8610@cluster0.hr2uuz8.mongodb.net/?appName=Cluster0")
db = cliente["iot"]
coleccion = db["humedad"]

@app.route('/humedad', methods=['POST'])
def recibir():
    data = request.get_json()
    data["fecha"] = datetime.now()
    coleccion.insert_one(data)
    return {"status": "ok"}

app.run(host='192.168.1.87', port=5000)