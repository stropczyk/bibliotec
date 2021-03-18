from pymongo import MongoClient

client = MongoClient('mongodb+srv://guest:guest-password@database.pjbt9.mongodb.net/bibliotec?retryWrites=true&w=majority')
db = client['bibliotec']
col = db['books']
