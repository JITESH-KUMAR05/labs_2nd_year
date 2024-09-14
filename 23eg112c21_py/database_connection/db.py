from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os

def get_database(db_name):
     # Hardcoded for demonstration; consider using environment variables
    CONNECTION_STRING = f"mongodb://localhost:27017/"

    # Create a connection using MongoClient
    client = MongoClient(CONNECTION_STRING)

    # Check if the connection is successful
    try:
        client.admin.command('ping')  # This command checks the connection
        print("Connected to MongoDB!")
    except ConnectionFailure:
        print("Failed to connect to MongoDB. Please check your connection settings.")

    # Create the database for our example
    return client[db_name]


item_1 = {
  "_id" : "U1IT00001",
  "item_name" : "Blender",
  "max_discount" : "10%",
  "batch_number" : "RR450020FRG",
  "price" : 340,
  "category" : "kitchen appliance"
}

item_2 = {
  "_id" : "U1IT00002",
  "item_name" : "Egg",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs jo vineel ko khane he"
}
item_3 = {
  "_id" : "U1IT00003",
  "item_name" : "Aanda",
  "category" : "food",
  "quantity" : 12,
  "price" : 36,
  "item_description" : "brown country eggs jo vineel ko khane he"
}
# This is added so that many files can reuse the function get_database()
if __name__ == "__main__":
    # Get the database name
    db_name = "shoping"

    # Get the database
    dbname = get_database(db_name)
    collection_name = dbname["user_1_detail"]
    collection_name.insert_many([item_1])
    collection_name.insert_many([item_3])

    
