import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database():
    CONNECTION_STRING = os.getenv("CONNECTION_STRING")
    client = MongoClient(CONNECTION_STRING)
    return client['hackysu']

if __name__ == "__main__":   
  
   # Get the database
   HackYSU = get_database()