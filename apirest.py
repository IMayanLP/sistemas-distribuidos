from datetime import date
from datetime import datetime

from fastapi import FastAPI

api = FastAPI()

@api.get("/")
def home():
    return "Bem-vindo"

@api.get("/data-hora")
def dataHora():
    return {"dia": date.today().day, "mês": date.today().month, "ano": date.today().year,
            "hora": datetime.now().strftime('%H:%M')}

@api.get("/converter/real-dolar/{num}")
def coversorRealDolar(num: float):
    return {"resultado": (num * 0.20)}

@api.get("/converter/dolar-real/{num}")
def coversorDolarReal(num: float):
    return {"resultado": (num * 4.97)}

@api.get("/converter/euro-real/{num}")
def coversorEuroReal(num: float):
    return {"resultado": (num * 5.39)}

@api.get("/converter/real-euro/{num}")
def coversorRealEuro(num: float):
    return {"resultado": (num * 0.19)}
