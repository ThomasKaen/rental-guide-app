from app.schemas.guide import Guide, LocalRecommendation

# Phase 1: hard-coded example guide.
# Replace with your real flat details.

GUIDES = [
    Guide(
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
        house_rules=[
            "No smoking inside the flat.",
            "No parties or events.",
            "Keep noise low after 22:00.",
            "Only registered guests are allowed to stay overnight.",
        ],
        appliances=[
            "Heating: thermostat is by the hallway. Turn knob to adjust temperature.",
            "Oven: press the power button, then select the temperature and mode.",
            "Washer-dryer: quick-wash program is 30°C, approx. 1 hour.",
            "TV: use the Samsung remote, HDMI1 is the streaming stick.",
        ],
        local_recommendations=[
            LocalRecommendation(
                name="Corner Market",
                type="shop",
                description="Small grocery store open 7am–11pm daily.",
                address="125 Example Street",
                map_url="https://maps.google.com",
            ),
            LocalRecommendation(
                name="Bella Pasta",
                type="restaurant",
                description="Casual Italian restaurant, good for dinner.",
                address="10 Food Lane",
                map_url="https://maps.google.com",
            ),
            LocalRecommendation(
                name="Tube Station",
                type="transport",
                description="Nearest underground station, 5–6 min walk.",
                address="Station Road",
                map_url="https://maps.google.com",
            ),
        ],
        emergency_info=(
            "For emergencies, dial 999 (police, ambulance, fire). "
            "For non-urgent medical advice, dial 111. "
            "Nearest hospital: Example Hospital, 1 Hospital Road."
        ),
    )
]
