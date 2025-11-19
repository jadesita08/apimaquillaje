from fastapi import APIRouter, HTTPException, status
from managers.ventasManager import VentasManager
from models.models import Venta 

router = APIRouter()
manager = VentasManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_venta(venta: Venta):
    venta_id = manager.crear_venta(venta)
    return {"id": venta_id, "mensaje": "Venta creada exitosamente"}

@router.get("/")
def obtener_ventas():
    ventas = manager.obtener_ventas()
    return ventas

@router.put("/{venta_id}")
def actualizar_venta(venta_id: int, venta: Venta):
    if not manager.actualizar_venta(venta_id, venta):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada o datos no actualizados")
    return {"mensaje": f"Venta con ID {venta_id} actualizada exitosamente"}

@router.delete("/{venta_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_venta(venta_id: int):
    if not manager.eliminar_venta(venta_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Venta no encontrada")
    return
