from pydantic import BaseModel
from typing import List, Optional


class LocalRecommendation(BaseModel):
    name: str
    type: str  # "restaurant", "shop", "transport", etc.
    description: str
    address: Optional[str] = None
    map_url: Optional[str] = None


class Guide(BaseModel):
    slug: str
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

    local_recommendations: List[LocalRecommendation]
    emergency_info: str
