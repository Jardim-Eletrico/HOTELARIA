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

'''
|===================================================|
|                    |HOSPEDE|                      |
|===================================================|
'''

#LISTAGEM

@app.get("/hospedes")
def get_hospedes(request: Request):
    hospedes = hospede_model.consulta_hospedes()

    return templates.TemplateResponse("index.html", {"request": request, "hospedes": hospedes})

#CADASTRO
@app.get("/add_hospede")
def add_hospede(request: Request):
    hospede = hospede_model.add_hospede()

    return templates.TemplateResponse("index.html", {"request": request, "hospede": hospede})