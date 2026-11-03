import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random
import json


app = FastAPI(title="Pokenea")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # fine for local dev; restrict in production
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_container_id():
    return os.environ.get("HOSTNAME", "Desconocido")

@app.get("/")
async def root():
    with open("neas.json",encoding = "utf-8") as f:
        data = json.load(f) 
    pokenea = random.choice(data)
    return {
        "id": pokenea.get("id"),
        "nombre": pokenea.get("nombre"),
        "altura": pokenea.get("altura"),
        "habilidad": pokenea.get("habilidad"),
        "frase": pokenea.get("frase"),
        "imagen": "images/images (1).jpg",
        "container_id": get_container_id()
    }

