from sqlalchemy import Column, Integer, String, Text
from app.core.database import Base


class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(100), unique=True, index=True, nullable=False)

    property_name = Column(String(255), nullable=False)
    address = Column(String(255), nullable=False)

    contact_phone = Column(String(50), nullable=False)
    contact_email = Column(String(255), nullable=False)

    wifi_name = Column(String(255), nullable=False)
    wifi_password = Column(String(255), nullable=False)

    checkin_time = Column(String(50), nullable=False)
    checkout_time = Column(String(50), nullable=False)
    checkin_instructions = Column(Text, nullable=False)
    checkout_instructions = Column(Text, nullable=False)

    house_rules_text = Column(Text, nullable=False)
    appliances_text = Column(Text, nullable=False)

    local_recommendations_text = Column(Text, nullable=False)
    emergency_info = Column(Text, nullable=False)
