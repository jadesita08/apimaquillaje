from managers.conexionManager import ConexionManager
from models.models import Venta

class VentasManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_venta(self, venta: Venta):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ventas (cliente_id, producto_id, cantidad, total) VALUES (%s, %s, %s, %s) RETURNING id",
            (venta.cliente_id, venta.producto_id, venta.cantidad, venta.total)
        )
        venta_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return venta_id
    
    def obtener_ventas(self):
        conn = self.conn_manager.get_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT id, cliente_id, producto_id, cantidad, total, fecha_venta FROM ventas")
        
        column_names = [desc[0] for desc in cursor.description]
        
        ventas = []
        for row in cursor.fetchall():
            venta_dict = dict(zip(column_names, row))
            if 'fecha_venta' in venta_dict and venta_dict['fecha_venta'] is not None:
                 venta_dict['fecha_venta'] = venta_dict['fecha_venta'].isoformat()
            ventas.append(venta_dict)
            
        cursor.close()
        conn.close()
        return ventas
    
    def eliminar_venta(self, venta_id: int):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM ventas WHERE id = %s", (venta_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_rows > 0
