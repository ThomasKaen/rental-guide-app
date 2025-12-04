from pydantic import BaseModel
from typing import List

class PropertyBase(BaseModel):
    property_name: str
    address: str
    contact_phone: str
    contact_email: str
    wifi_name: str
    wifi_password: str
    checkin_time: str
    checkout_time: str
    checkin_instructions: str
    checkout_instructions: str
    house_rules: List[str]
    appliances: List[str]
    local_recommendations_text: str
    emergency_info: str

class PropertyCreate(PropertyBase):
    slug: str

class PropertyUpdate(BaseModel):
    property_name: str
    address: str

    contact_phone: str
    contact_email: str

    wifi_name: str
    wifi_password: str

    checkin_time: str
    checkout_time: str
    checkin_instructions: str
    checkout_instructions: str

    house_rules: List[str]
    appliances: List[str]

    local_recommendations_text: str
    emergency_info: str
