import pymongo
client = pymongo.MongoClient("mongodb+srv://root:<Dhani@14630123@cluster0.sohp6.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)


d = {"name": "manoj",
     "email": "manojsharma7376@wipro.com",
     "last": "sharma"
}
bd1 = client1['mongotest']
coll = db1['test']
coll.insert_one(d)


afjksj
sdfsfk
asdfsf