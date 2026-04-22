from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"status": "ok", "mensaje": "Tu plataforma está viva 🚀"}