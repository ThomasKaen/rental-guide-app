from typing import Optional, List

from sqlalchemy.orm import Session

from app.core.database import SessionLocal, engine, Base
from app.models.property import Property
from app.schemas.property import PropertyUpdate


# Make sure tables exist
Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_property_by_slug(db: Session, slug: str) -> Optional[Property]:
    return db.query(Property).filter(Property.slug == slug).first()

def get_all_properties(db: Session) -> List[Property]:
    """Return all properties ordered by name."""
    return db.query(Property).order_by(Property.property_name).all()

def ensure_seed_property(db: Session):
    """Create an initial example property if none exists."""
    existing = get_property_by_slug(db, "company-flat-1")
    if existing:
        return

    prop = Property(
        slug="company-flat-1",
        property_name="Company Flat – Central Apartment",
        address="123 Example Street, London",
        contact_phone="+44 1234 567890",
        contact_email="support@company.com",
        wifi_name="CompanyFlatWiFi",
        wifi_password="SuperSecure123",
        checkin_time="15:00",
        checkout_time="11:00",
        checkin_instructions=(
            "Use the code sent in your booking message to open the main door. "
            "The flat is on the 3rd floor, door 3B. Keys are in the lockbox "
            "next to the door."
        ),
        checkout_instructions=(
            "Please check out by 11:00. Leave keys on the table and close the "
            "door behind you. Rubbish can be taken to the bins in the courtyard."
        ),
        house_rules_text="\n".join(
            [
                "No smoking inside the flat.",
                "No parties or events.",
                "Keep noise low after 22:00.",
                "Only registered guests are allowed to stay overnight.",
            ]
        ),
        appliances_text="\n".join(
            [
                "Heating: thermostat is by the hallway. Turn knob to adjust temperature.",
                "Oven: press the power button, then select the temperature and mode.",
                "Washer-dryer: quick-wash program is 30°C, approx. 1 hour.",
                "TV: use the Samsung remote, HDMI1 is the streaming stick.",
            ]
        ),
        local_recommendations_text=(
            "Corner Market (shop): Small grocery store open 7am–11pm daily.\n"
            "Bella Pasta (restaurant): Casual Italian restaurant, good for dinner.\n"
            "Tube Station (transport): Nearest underground station, 5–6 min walk."
        ),
        emergency_info=(
            "For emergencies, dial 999 (police, ambulance, fire). "
            "For non-urgent medical advice, dial 111. "
            "Nearest hospital: Example Hospital, 1 Hospital Road."
        ),
    )
    db.add(prop)
    db.commit()


def update_property_from_schema(
    db: Session, prop: Property, data: PropertyUpdate
) -> Property:
    prop.property_name = data.property_name
    prop.address = data.address

    prop.contact_phone = data.contact_phone
    prop.contact_email = data.contact_email

    prop.wifi_name = data.wifi_name
    prop.wifi_password = data.wifi_password

    prop.checkin_time = data.checkin_time
    prop.checkout_time = data.checkout_time
    prop.checkin_instructions = data.checkin_instructions
    prop.checkout_instructions = data.checkout_instructions

    prop.house_rules_text = "\n".join(
        [r.strip() for r in data.house_rules if r.strip()]
    )
    prop.appliances_text = "\n".join(
        [a.strip() for a in data.appliances if a.strip()]
    )

    prop.local_recommendations_text = data.local_recommendations_text
    prop.emergency_info = data.emergency_info

    db.add(prop)
    db.commit()
    db.refresh(prop)
    return prop
