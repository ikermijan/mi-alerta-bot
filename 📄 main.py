from fastapi import FastAPI
from pydantic import BaseModel
import feedparser

app = FastAPI()

intereses = []

class Interes(BaseModel):
    nombre: str

@app.get("/")
def home():
    return {"status": "ok"}

@app.post("/intereses")
def add_interes(interes: Interes):
    intereses.append(interes.nombre)
    return {"intereses": intereses}

@app.get("/intereses")
def get_intereses():
    return {"intereses": intereses}

# 🔥 NUEVO: buscar info
@app.get("/buscar")
def buscar():
    resultados_finales = []

    for interes in intereses:
        url = f"https://news.google.com/rss/search?q={interes}"
        feed = feedparser.parse(url)

        for entry in feed.entries[:5]:
            resultados_finales.append({
                "interes": interes,
                "titulo": entry.title,
                "link": entry.link
            })

    return {"resultados": resultados_finales}
