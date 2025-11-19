from fastapi import APIRouter, HTTPException, status
from managers.clientesManager import ClientesManager
from models import Cliente 

router = APIRouter()
manager = ClientesManager()

@router.post("/", status_code=status.HTTP_201_CREATED)
def crear_cliente(cliente: Cliente):
    # La validación de fallos se deja al framework/Manager si falla
    cliente_id = manager.crear_cliente(cliente)
    return {"id": cliente_id, "mensaje": "Cliente creado exitosamente"}

@router.get("/")
def obtener_clientes():
    clientes = manager.obtener_clientes()
    return clientes

@router.put("/{cliente_id}")
def actualizar_cliente(cliente_id: int, cliente: Cliente):
    # Se mantiene la verificación de 404 para actualizar, ya que es lógica de negocio
    if not manager.actualizar_cliente(cliente_id, cliente):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado o datos no actualizados")
    return {"mensaje": f"Cliente con ID {cliente_id} actualizado exitosamente"}

@router.delete("/{cliente_id}", status_code=status.HTTP_204_NO_CONTENT)
def eliminar_cliente(cliente_id: int):
    # Se mantiene la verificación de 404 para eliminar
    if not manager.eliminar_cliente(cliente_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Cliente no encontrado")
    return