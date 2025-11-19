from managers.conexionManager import ConexionManager
from models.models import Producto

class ProductosManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_producto(self, producto: Producto):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO productos (nombre, marca, categoria, precio, stock) VALUES (%s, %s, %s, %s, %s) RETURNING id",
            (producto.nombre, producto.marca, producto.categoria, producto.precio, producto.stock)
        )
        producto_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return producto_id
    
    def obtener_productos(self):
        conn = self.conn_manager.get_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, marca, categoria, precio, stock FROM productos")
        
        column_names = [desc[0] for desc in cursor.description]
        productos = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            
        cursor.close()
        conn.close()
        return productos
    
    def actualizar_producto(self, producto_id: int, producto: Producto):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET nombre = %s, marca = %s, categoria = %s, precio = %s, stock = %s WHERE id = %s",
            (producto.nombre, producto.marca, producto.categoria, producto.precio, producto.stock, producto_id)
        )
        updated_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated_rows > 0
    
    def eliminar_producto(self, producto_id: int):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM productos WHERE id = %s", (producto_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_rows > 0
