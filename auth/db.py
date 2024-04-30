# config your Client and collection name
from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.environ.get("MONGO_URI")




#Function add one data to mongoDB
def get_next_sequence_value(collection_name):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["DataTest"]
    col = db[collection_name]
    last_doc = col.find_one({}, sort=[('_id', -1)], projection={'_id': 1})
    next_id = 1 if last_doc is None else last_doc['_id'] + 1  
    return next_id

def add_data_to_mongodb(data):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["DataTest"]
    col = db["Table"]
    next_id = get_next_sequence_value("Table")
    data['_id'] = next_id
    col.insert_one(data)
    

def update_data_to_mongodb(current_id, data):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test") 
    db = client["DataTest"]
    col = db["Table"]
    filter_query = {"_id": current_id}
    update_data = {"$set": data.dict()}
    col.update_one(filter_query, update_data)
  
#Function delete one data in mongoDB
def delete_result_in_mongo(id):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test") 
    db = client["DataTest"]
    col = db["Table"]
    col.delete_one({"_id": id})
      
#Function add user to mongoDB   
def dataMong_user():
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["user"]
    col = db["datauser"]
    cursor = col.find()
    return list(cursor)
users = dataMong_user()

def get_next_sequence_value_for_user(collection):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["user"]
    col = db[collection]
    last_doc = col.find_one({}, sort=[('_id', -1)], projection={'_id': 1})
    next_id = 1 if last_doc is None else last_doc['_id'] + 1  
    return next_id


def add_data_user_to_mongodb(data):
    client = MongoClient("mongodb+srv://innedhelp123456:25Jg8gtjyCfh61jq@test.w5z7ngz.mongodb.net/?retryWrites=true&w=majority&appName=Test")
    db = client["user"]
    col = db["datauser"]
    next_id = get_next_sequence_value_for_user("datauser")
    data['_id'] = next_id
    col.insert_one(data)
    
