from pymongo import MongoClient

MONGO_URI = "mongodb+srv://2124300362_db_user:12641801@cluster0.pnos3vb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = MongoClient(MONGO_URI)
db = client["zapateria"]
usuarios_collection = db["usuarios"]

print("Usuarios registrados:")
for u in usuarios_collection.find():
    print(u)