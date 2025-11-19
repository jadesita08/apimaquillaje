from fastapi import APIRouter, HTTPException, status
from managers.ventasManager import VentasManager
from models import Venta 

router = APIRouter()
manager = VentasManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_venta(venta: Venta):
    # La validación de fallos se deja al framework/Manager si falla
    venta_id = manager.crear_venta(venta)
    return {"id": venta_id, "mensaje": "Venta creada exitosamente"}

@router.get("/")
def obtener_ventas():
    ventas = manager.obtener_ventas()
    return ventas

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: int):
    if not manager.eliminar_venta(venta_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
    return