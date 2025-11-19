from fastapi import APIRouter, HTTPException, status
from managers.productosManager import ProductosManager
from models import Producto 

router = APIRouter()
manager = ProductosManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_producto(producto: Producto):
    # La validación de fallos se deja al framework/Manager si falla
    producto_id = manager.crear_producto(producto)
    return {"id": producto_id, "mensaje": "Producto creado exitosamente"}

@router.get("/")
def obtener_productos():
    productos = manager.obtener_productos()
    return productos

@router.put("/{producto_id}")
def actualizar_producto(producto_id: int, producto: Producto):
    if not manager.actualizar_producto(producto_id, producto):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado o datos no actualizados")
    return {"mensaje": f"Producto con ID {producto_id} actualizado exitosamente"}

@router.delete("/{producto_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_producto(producto_id: int):
    if not manager.eliminar_producto(producto_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Producto no encontrado")
    return