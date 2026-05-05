from fastapi import FastAPI
from routes import idps, steg, incidents

app = FastAPI()

app.include_router(idps.router)
app.include_router(steg.router)
app.include_router(incidents.router)