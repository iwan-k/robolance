from typing import Union, List
from fastapi import FastAPI, Request, Form
from fastapi.params import Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from database import engine, Base, get_db
from models import RobolancerDB
from schemas import Robolancer


templates = Jinja2Templates(directory="templates")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
async def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/healthcheck")
def healthcheck():
    return {"OK": 200}


@app.get("/")
def redirect():
    return RedirectResponse("/index")


@app.get("/index", response_class=HTMLResponse)
async def index(request: Request):
    if "g-recaptcha-response" in request.query_params:
        return templates.TemplateResponse("redirect.html", {"request": request})
    return templates.TemplateResponse("index.html", {"request": request})


@app.get('/robolancer')
async def list_robolancer(request: Request, db: Session = Depends(get_db)):
    db_robolancer_list = db.query(RobolancerDB).all()
    data = [Robolancer(**item.__dict__) for item in db_robolancer_list]
    return templates.TemplateResponse("robolancer.html", {"request": request, "data": data})
