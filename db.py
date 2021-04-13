import motor.motor_asyncio

MONGO_DETAILS = "mongodb://habitanto:yV9uAceDbPvNFu3RhEjJ0deGLocL0UIP88ts9z2Ox2zPwEENjMF6CEuFPOdbzDwYoJqmhWI8aGLobg0voj3OXg==@habitanto.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@habitanto@"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)