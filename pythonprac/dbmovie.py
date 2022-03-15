from pymongo import MongoClient
client = MongoClient('mongodb+srv://test:sparta@cluster0.zv3yk.mongodb.net/cluster0?retryWrites=true&w=majority')
db = client.dbsparta

db.movies.update_one({'title':'가버나움'},{'$set':{'star': '0'}})