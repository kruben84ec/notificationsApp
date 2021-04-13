from NotificationApp import NotificationApp
from db import client
from fastapi import FastAPI, Body, APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# Add a new notification into to the database
async def add_notication(notification_data: dict) -> dict:
    database = client.habitanto_data
    notification_collection = database.get_collection("NotificationApp")
    student = await notification_collection.insert_one(notification_data)
    new_student = await notification_collection.find_one({"_id": student.inserted_id})
    return notification_helper(new_student)


def notification_helper(notification_row) -> dict:
    return {
        "message": notification_row["message"],
        "segment": notification_row["segment"]
    }



@app.get("/notification/list/{limit}")
async def notification(limit:int):
    if not limit:
        limit = 10
    notification_list = []
    database = client.habitanto_data
    notification_collection = database.get_collection("NotificationApp")
    async for notification_row in notification_collection.find().limit(limit):
        notification_list.append(notification_helper(notification_row))

    return notification_list


@app.post("/notification",  response_description="Notification data added into the database")
async def notification(notification_message: NotificationApp = Body(...)):
    notification_data = jsonable_encoder(notification_message)
    new_notification = await add_notication(notification_data)
    return {"data": new_notification}