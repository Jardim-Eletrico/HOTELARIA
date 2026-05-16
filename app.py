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

@app.get("/")
def root(request: Request):
    hospedes = hospede_model.consulta_hospedes()
    quartos = quarto_model.consulta_quartos()
    reservas = reserva_model.consulta_reservas()

    return templates.TemplateResponse("index.html", {"request": request, "hospedes": hospedes, "quartos": quartos, "reservas": reservas})