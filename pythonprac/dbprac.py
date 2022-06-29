from pymongo import MongoClient
client = MongoClient('여기에 URL 입력')
db = client.dbsparta

doc = {
    'name': 'bob',
    'age': 27
}

db.users.insert_one(doc)
