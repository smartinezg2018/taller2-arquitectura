import os
import json
import random
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Pokenea")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_container_id():
    return os.environ.get("HOSTNAME", "Desconocido")

# Ruta 1: Devuelve el JSON del Pokenea
@app.get("/api/pokenea")
async def get_pokenea_json():
    with open("neas.json", encoding="utf-8") as f:
        data = json.load(f) 
    pokenea = random.choice(data)
    return {
        "id": pokenea.get("id"),
        "nombre": pokenea.get("nombre"),
        "altura": pokenea.get("altura"),
        "habilidad": pokenea.get("habilidad"),
        "frase": pokenea.get("frase"),
        "imagen": pokenea.get("imagen"), # Asegúrate de que esto venga del bucket de GCP
        "container_id": get_container_id()
    }

# Ruta 2: Devuelve la interfaz gráfica (HTML)
@app.get("/")
async def root_html():
    return FileResponse("index.html")