from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import scraper

app = FastAPI(title="DSR ScrapAssist V4")
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True, allow_methods=["*"], allow_headers=["*"])

class SearchParams(BaseModel):
    commune: str
    rayon: int
    effectif: str
    statut: str
    telephone: bool
    email: bool

@app.post("/search")
def search(data: SearchParams):
    try:
        return {"results": scraper.run(data.dict())}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
