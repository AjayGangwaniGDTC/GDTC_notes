#MongoDB connection and working with mongodb database
#mongoDB is document based Database management system
#also known as NoSQL
#It is capable of working with JSON and CSV format data
#It supports also kind of long,int,str,float,obj datatypes
# {} records inside curly bracket considered as an object
# [] records inside square bracket consider as an array like json
# to perform database connectivity 


#to install mongodb in jupyter notebook type 
#conda install pymongo
#pip install pymongo

import pymongo

def getConn():
    #create a client object to get connected with mongo client
    client=pymongo.MongoClient("mongodb://localhost:27017/")
    #get list of database available on connection url
    #print(client.list_database_names())
    dblist=client.list_database_names()
    if "TestMongoDB" in dblist:
        print("Database already exists")
    #we choose the database from client connection
    conn=client["TestMongoDB"]
    return conn

conn=getConn()
mydata=conn['customers'] #name of the table is customers
print(type(mydata))

#Inserting the values into the database with table
# listcust=[{"id":102,"name":"krishna","age":21}, {"id":103,"name":"Devi","age":24}]
# data=mydata.insert_many(listcust)
# print(data.inserted_ids)

for i in mydata.find():
    print(i)
    
for i in mydata.find({},{"_id":0,"id":1,"name":1,"age":1}): #finding the values in the data table we are omiting the _id key as it is 0 and also printing all other values as it is 1
    print(i)
    
for i in mydata.find({},{"age":0}): #printing all records by omiting age
    print(i)

#filter records using query
myquery={"age":21}
data=mydata.find(myquery)
for i in data:
    print(i)
    
#sorting the data by age in ascending order
data =mydata.find.sort("age")
for i in data:
    print(i)
    
#sorting the data by age in descending order
data =mydata.find.sort("age", -1)
for i in data:
    print(i)
    
# #deleting a single value with id 101
# myquery={"id":101}
# mydata.delete_one(myquery)

# #deleting all the values in the database
# myquery={}
# mydata.delete_many(myquery)