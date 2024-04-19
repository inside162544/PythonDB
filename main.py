from dotenv import load_dotenv,find_dotenv
import os
import pprint
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")


connection_string =   f"mongodb+srv://inside162544:{password}@pythondb.piijqhq.mongodb.net/?retryWrites=true&w=majority&appName=PythonDB"
client = MongoClient(connection_string)

dbs = client.list_database_names()
DormitoryDB = client["DormitoryDB"]
collections = DormitoryDB.list_collection_names()
print(collections)

## user for add data in data base in mongoDB ##

def insert_Dormitory_doc():
    collections = DormitoryDB.Dormitory
    Dormitory_document = {
        "Name" : "Dormitory01",
        "type" : "name"
    }
    inserted_id = collections.insert_one(Dormitory_document).inserted_id
    print(inserted_id)

home = client.home
DormitoryDB_collcetion = home.DormitoryDB_collcetion


##  use For Create like table in mongo and add data in the same times ##
def create_documents():
    name = [ "HappyHouse","LoveHouse","DreamHouse","WorkHouse","GoodHouse"]
    address = ["Thai","Silom","bangrak","bangpo","bangoo"]
    rent = ["10000","12000","8000","9000","7000"]

    docs = []

    for name,address,rent in zip(name,address,rent):
        doc = {"name":name, "address":address,"rent":rent}
        docs.append(doc)
        # address.insert_one(doc)
    DormitoryDB_collcetion.insert_many(docs)

printer = pprint.PrettyPrinter()


##  use for fine data in database MongoDB ##
def find_all_house(): 
    house = DormitoryDB_collcetion.find()
   
    # print(list(house)) ใช้สำหรับ get ID object 

    for   home in house:
        printer.pprint(home)


##
def find_happyhouse():
    happyhouse = home.find_one({"name" : "Happyhouse"})
    printer.pprint(happyhouse)

find_happyhouse()