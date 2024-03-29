from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import os

app = FastAPI()

# Get the path to the templates folder
templates_dir = os.path.join(os.path.dirname(__file__), "../templates")

# Initialize Jinja2Templates instance
templates = Jinja2Templates(directory=templates_dir)

# Get the path to the static folder
static_dir = os.path.join(os.path.dirname(__file__), "../static")

# Mount the static directory
app.mount("/static", StaticFiles(directory=static_dir), name="static")

# Define route handlers
@app.get("/", response_class=HTMLResponse)
async def home_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/contact", response_class=HTMLResponse)
async def contact_page(request: Request):
    return templates.TemplateResponse("contact.html", {"request": request})

@app.get("/about", response_class=HTMLResponse)
async def about_page(request: Request):
    return templates.TemplateResponse("about.html", {"request": request})
