from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
import feedparser

app = FastAPI()

intereses = []

@app.get("/", response_class=HTMLResponse)
def home():
    return """
    <h2>Buscador de intereses</h2>
    <form action="/buscar" method="post">
        <input name="interes" placeholder="ej: ciberseguridad">
        <button type="submit">Buscar</button>
    </form>
    """

@app.post("/buscar", response_class=HTMLResponse)
def buscar(interes: str = Form(...)):
    url = f"https://news.google.com/rss/search?q={interes}"
    feed = feedparser.parse(url)

    html = f"<h2>Resultados para: {interes}</h2>"

    for entry in feed.entries[:10]:
        html += f'<p><a href="{entry.link}" target="_blank">{entry.title}</a></p>'

    return html
