from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI()


class Item(BaseModel):
    nombre: str
    precio: int
    disponible: bool = True


class User(BaseModel):
    nombre: str = Field(..., min_lengths=3)
    email: str = Field(...)
    edad: int = Field(..., ge=18)


@app.get("/")
def root():
    return {"Mensaje:": "Api funcionando correctamente"}


@app.get("/info")
def info():
    return {"Nombre": "Creando api"}


@app.get("/productos/{id}")
def productos(id: int):
    return {"msg": "Producto encontrado", "id": "123"}


@app.post("/productos")
def crear_producto(item: Item):
    return {"msg": "Producto creado"}


@app.post("/usuarios", status_code=201)
def crear_usuarios(user: User):
    return {"msg": "Creado con exito", "usuario_creado": user}


@app.get("/usuarios/{id}")
def search_user_id(id: int):
    if id not in (1, 2):
        raise HTTPException(status_code=404, detail="Not found")
    else:
        return {"msg": "Found succed", "user_id": id}
