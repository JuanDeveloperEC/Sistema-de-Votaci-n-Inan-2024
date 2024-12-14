from fastapi import FastAPI,Depends, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from Database.mySql import getbd , SessionLocal

import jinja2

print("Jinja2 está disponible:", jinja2._version_)

app = FastAPI() 

app.mount("/static",StaticFiles(directory="static"),name="static")
templates = Jinja2Templates(directory="templates")


@app.get("/",response_class = HTMLResponse)
async def home (request:Request):
    return templates.TemplateResponse("home.html", {
        "request":request
    })

#@app.get("/BuscarUsuarios")
#def buscarusuarios(cedula:str, db:SessionLocal=Depends(getbd)):
    #usuarios = db.queary(usuarios).filter(usuarios.cedula.ilke(f"{cedula}")).all()
    #return usuarios

@app.post("/RegistrarVoto")
def registrarvoto():
    return 0

