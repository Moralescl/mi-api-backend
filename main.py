from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configuramos el "guardia de seguridad" para permitir que tu HTML se conecte
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # El asterisco significa "deja entrar a cualquiera" (ideal para aprender)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def leer_raiz():
    return {"mensaje": "¡Hola mundo! Mi primera API está viva y conectada"}