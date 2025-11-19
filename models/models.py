from pydantic import BaseModel

class Cliente(BaseModel):
    nombre: str
    email: str
    telefono: str

class Producto(BaseModel):
    nombre: str
    marca: str
    categoria: str
    precio: float
    stock: int

class Venta(BaseModel):
    cliente_id: int
    producto_id: int
    cantidad: int
    total: float