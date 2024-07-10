from motor.motor_asyncio import AsyncIOMotorClient

HOST = "mongodb://localhost:27017"

client = AsyncIOMotorClient(HOST)

database = client.library

book_collection = database.get_collection("books")
user_collection = database.get_collection("users")
loan_collection = database.get_collection("loans")