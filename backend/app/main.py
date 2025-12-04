from fastapi import FastAPI, Request, HTTPException, Form, Depends, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import get_settings
from app.core.database import Base, engine
from app.services.property_service import (
    get_db,
    get_property_by_slug,
    ensure_seed_property,
    update_property_from_schema,
    get_all_properties,
    create_property_from_schema,
)
from app.schemas.property_schemas import PropertyUpdate, PropertyCreate

settings = get_settings()

# Ensure tables exist
Base.metadata.create_all(bind=engine)

app = FastAPI(title=settings.PROJECT_NAME)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup_event():
    # Make sure we have at least the seed property
    from sqlalchemy.orm import Session

    db: Session = next(get_db())
    ensure_seed_property(db)


@app.get("/health", tags=["system"])
async def health_check():
    return {"status": "ok"}


@app.get("/guide/{slug}", response_class=HTMLResponse, tags=["guides"])
async def guide_page(request: Request, slug: str, db=Depends(get_db)):
    prop = get_property_by_slug(db, slug)
    if not prop:
        raise HTTPException(status_code=404, detail="Guide not found")

    house_rules = [
        line for line in (prop.house_rules_text or "").splitlines() if line.strip()
    ]
    appliances = [
        line for line in (prop.appliances_text or "").splitlines() if line.strip()
    ]
    local_recs = [
        line
        for line in (prop.local_recommendations_text or "").splitlines()
        if line.strip()
    ]

    guide = {
        "slug": prop.slug,
        "property_name": prop.property_name,
        "address": prop.address,
        "contact_phone": prop.contact_phone,
        "contact_email": prop.contact_email,
        "wifi_name": prop.wifi_name,
        "wifi_password": prop.wifi_password,
        "checkin_time": prop.checkin_time,
        "checkout_time": prop.checkout_time,
        "checkin_instructions": prop.checkin_instructions,
        "checkout_instructions": prop.checkout_instructions,
        "house_rules": house_rules,
        "appliances": appliances,
        "local_recommendations": local_recs,
        "emergency_info": prop.emergency_info,
    }

    return templates.TemplateResponse(
        "guide.html",
        {
            "request": request,
            "guide": guide,
        },
    )


@app.get("/admin", include_in_schema=False)
async def admin_root():
    return RedirectResponse(url="/admin/properties")

@app.get(
    "/admin/properties",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def list_properties_page(request: Request, db=Depends(get_db)):
    props = get_all_properties(db)
    return templates.TemplateResponse(
        "admin_property_list.html",
        {
            "request": request,
            "properties": props,
        },
    )

@app.get("/admin/properties/new", response_class=HTMLResponse, include_in_schema=False)
async def new_property_page(request: Request):
    defaults = dict(
        property_name="", slug="", address="",
        contact_phone="", contact_email="",
        wifi_name="", wifi_password="",
        checkin_time="15:00", checkout_time="11:00",
        checkin_instructions="", checkout_instructions="",
        house_rules_text="", appliances_text="",
        local_recommendations_text="",
        emergency_info="For emergencies, dial 999. For non-urgent medical advice, dial 111.",
        error=None,
    )
    return templates.TemplateResponse("admin_property_new.html", {"request": request, **defaults})

@app.post("/admin/properties/new", response_class=HTMLResponse, include_in_schema=False)
async def create_property(
    request: Request,
    db=Depends(get_db),
    property_name: str = Form(...),
    slug: str = Form(...),
    address: str = Form(...),
    contact_phone: str = Form(...),
    contact_email: str = Form(...),
    wifi_name: str = Form(...),
    wifi_password: str = Form(...),
    checkin_time: str = Form(...),
    checkout_time: str = Form(...),
    checkin_instructions: str = Form(""),
    checkout_instructions: str = Form(""),
    house_rules_text: str = Form(""),
    appliances_text: str = Form(""),
    local_recommendations_text: str = Form(""),
    emergency_info: str = Form(""),
):
    slug = slug.strip()
    error = None
    if not slug:
        error = "Slug is required."
    elif " " in slug:
        error = "Slug cannot contain spaces (use dashes)."

    if error:
        return templates.TemplateResponse(
            "admin_property_new.html",
            {
                "request": request,
                "property_name": property_name, "slug": slug, "address": address,
                "contact_phone": contact_phone, "contact_email": contact_email,
                "wifi_name": wifi_name, "wifi_password": wifi_password,
                "checkin_time": checkin_time, "checkout_time": checkout_time,
                "checkin_instructions": checkin_instructions, "checkout_instructions": checkout_instructions,
                "house_rules_text": house_rules_text, "appliances_text": appliances_text,
                "local_recommendations_text": local_recommendations_text,
                "emergency_info": emergency_info,
                "error": error,
            },
        )

    data = PropertyCreate(
        property_name=property_name, slug=slug, address=address,
        contact_phone=contact_phone, contact_email=contact_email,
        wifi_name=wifi_name, wifi_password=wifi_password,
        checkin_time=checkin_time, checkout_time=checkout_time,
        checkin_instructions=checkin_instructions, checkout_instructions=checkout_instructions,
        house_rules=[l for l in house_rules_text.splitlines()],
        appliances=[l for l in appliances_text.splitlines()],
        local_recommendations_text=local_recommendations_text,
        emergency_info=emergency_info,
    )

    try:
        create_property_from_schema(db, data)
    except ValueError as e:
        return templates.TemplateResponse(
            "admin_property_new.html",
            {
                "request": request,
                **data.dict(),
                "house_rules_text": house_rules_text,
                "appliances_text": appliances_text,
                "error": str(e),
            },
        )

    return RedirectResponse(url=f"/admin/properties/{slug}/edit", status_code=303)

@app.get(
    "/admin/properties/{slug}/edit",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def edit_property_page(request: Request, slug: str, db=Depends(get_db)):
    prop = get_property_by_slug(db, slug)

    if not prop:
        ensure_seed_property(db)
        prop = get_property_by_slug(db, slug)

    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")

    house_rules = prop.house_rules_text or ""
    appliances = prop.appliances_text or ""

    return templates.TemplateResponse(
        "admin_property_edit.html",
        {
            "request": request,
            "prop": prop,
            "house_rules_text": house_rules,
            "appliances_text": appliances,
        },
    )


@app.post(
    "/admin/properties/{slug}/edit",
    response_class=HTMLResponse,
    include_in_schema=False,
)
async def update_property(
    request: Request,
    slug: str,
    db=Depends(get_db),
    property_name: str = Form(...),
    address: str = Form(...),
    contact_phone: str = Form(...),
    contact_email: str = Form(...),
    wifi_name: str = Form(...),
    wifi_password: str = Form(...),
    checkin_time: str = Form(...),
    checkout_time: str = Form(...),
    checkin_instructions: str = Form(...),
    checkout_instructions: str = Form(...),
    house_rules_text: str = Form(...),
    appliances_text: str = Form(...),
    local_recommendations_text: str = Form(...),
    emergency_info: str = Form(...),
):
    prop = get_property_by_slug(db, slug)
    if not prop:
        raise HTTPException(status_code=404, detail="Property not found")

    data = PropertyUpdate(
        property_name=property_name,
        address=address,
        contact_phone=contact_phone,
        contact_email=contact_email,
        wifi_name=wifi_name,
        wifi_password=wifi_password,
        checkin_time=checkin_time,
        checkout_time=checkout_time,
        checkin_instructions=checkin_instructions,
        checkout_instructions=checkout_instructions,
        house_rules=[line for line in house_rules_text.splitlines()],
        appliances=[line for line in appliances_text.splitlines()],
        local_recommendations_text=local_recommendations_text,
        emergency_info=emergency_info,
    )

    update_property_from_schema(db, prop, data)

    return RedirectResponse(
        url=f"/admin/properties/{slug}/edit",
        status_code=303,
    )
