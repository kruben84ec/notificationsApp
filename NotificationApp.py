from typing import Optional
from pydantic import BaseModel

class NotificationApp(BaseModel):
    message: str
    segment: Optional[str] = None
    quality: str
    status: Optional[str] = None
    email: str
    create: str
    auth: str
    address: str
    phone: str
    password: str
    textbody: str
    control: str
    catality: str
