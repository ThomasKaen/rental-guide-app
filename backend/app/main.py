from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.core.config import get_settings
from app.services.guide_service import get_guide_by_slug

settings = get_settings()

app = FastAPI(title=settings.PROJECT_NAME)

# Static files (for CSS, images later)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")


@app.get("/health", tags=["system"])
async def health_check():
    return {"status": "ok"}


@app.get("/guide/{slug}", response_class=HTMLResponse, tags=["guides"])
async def get_guide_page(request: Request, slug: str):
    guide = get_guide_by_slug(slug)
    if not guide:
        raise HTTPException(status_code=404, detail="Guide not found")

    return templates.TemplateResponse(
        "guide.html",
        {
            "request": request,
            "guide": guide,
        },
    )
