from fastapi import FastAPI, Request, Form, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from model import Hospede, Quarto, Reserva

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

hospede_model = Hospede()
quarto_model = Quarto()
reserva_model = Reserva()