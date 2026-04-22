from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Aquí guardamos intereses (temporal, luego irá a DB)
intereses = []

class Interes(BaseModel):
    nombre: str

@app.get("/")
def home():
    return {"status": "ok", "mensaje": "Tu plataforma está viva 🚀"}

# 👉 Añadir interés
@app.post("/intereses")
def add_interes(interes: Interes):
    intereses.append(interes.nombre)
    return {"ok": True, "intereses": intereses}

# 👉 Ver intereses
@app.get("/intereses")
def get_intereses():
    return {"intereses": intereses}
