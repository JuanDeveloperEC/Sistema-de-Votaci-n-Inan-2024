from typing import Dict
from fastapi import FastAPI, Form, HTTPException, Request , Depends
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
#from Database.mySql import Session
from pydantic import BaseModel
from sqlalchemy.orm import Session
from Database.mySql import Votaciones, getbd,Usuarios
import jinja2

print("Jinja2 está disponible:", jinja2.__version__)

app = FastAPI() 

app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="template")


@app.get("/", response_class= HTMLResponse)
async def home(request:Request):
    return templates.TemplateResponse("home.html", {
        "request": request
    })

@app.get("/votacion", response_class= HTMLResponse)
async def votacion(request:Request):
    return templates.TemplateResponse("votacion.html", {
        "request": request
    })

@app.get("/BuscarUsuarios")
def buscarusuarios(cedula:str, db:Session =Depends(getbd)):
    usuario = db.query(Usuarios).filter(Usuarios.cedula == cedula).first()
    if usuario:
        if usuario.estado == False:  # Verifica si el usuario ya votó
            return JSONResponse(content={"success": False, "message": "El usuario ya ha votado."},status_code=403)
        
        # Actualiza el estado del usuario a False ( que este ya votó) (activar el sabado)
        usuario.estado = False
        db.commit()

        return JSONResponse(content={"success": True, "nombre": f"{usuario.nombre} {usuario.apellido}"})
    else:
        return JSONResponse(content={"success": False, "message": "Cédula no encontrada"}, status_code=404)
    
   
class Voto(BaseModel):
    voto: int

@app.post("/RegistrarVoto")
async def registrar_voto(voto: Voto, db: Session = Depends(getbd)):
    # Verificar si el voto es válido
    if voto.voto not in [1, 2, 3, 4]:
        raise HTTPException(status_code=400, detail="Voto inválido")
    
    # Crear el objeto de voto para agregar a la base de datos
    nuevo_voto = Votaciones(voto=voto.voto)
    db.add(nuevo_voto)
    db.commit()  # Confirmar la transacción
    db.refresh(nuevo_voto)  # Obtener el voto actualizado con el ID generado
    
    return {"mensaje": "Voto registrado con éxito", "id_voto": nuevo_voto.idvotaciones}
    

  


     
    
