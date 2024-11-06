from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from core.system import System

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="templates"), name="static")

@app.get('/')
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/champion/{name}", response_class=HTMLResponse)
async def champion_info(request: Request, name: str):
    champion_data = System(name)

    if not champion_data.info or not champion_data.quotes:
        return HTMLResponse(content="Erro ao buscar informações do campeão.", status_code=500)

    return templates.TemplateResponse("champion.html", {
        "request": request,
        "name": name,
        "info": champion_data.info,
        "quotes": champion_data.quotes
    })
