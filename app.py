from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import scraper

app = FastAPI(title="DSR ScrapAssist V4")

# Montre le dossier frontend sur /app
app.mount("/app", StaticFiles(directory="frontend", html=True), name="static")

# API REST
class SearchParams(BaseModel):
    commune: str
    rayon: int
    effectif: str
    statut: str
    telephone: bool
    email: bool

@app.post("/search")
def search(data: SearchParams):
    return {"results": scraper.run(data.dict())}

# Redirection racine → /app
@app.get("/")
def root():
    return {"redirect": "/app"}
