from managers.conexionManager import ConexionManager
from models.models import Cliente

class ClientesManager:
    def __init__(self):
        self.conn_manager = ConexionManager()
    
    def crear_cliente(self, cliente: Cliente):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO clientes (nombre, email, telefono) VALUES (%s, %s, %s) RETURNING id",
            (cliente.nombre, cliente.email, cliente.telefono)
        )
        cliente_id = cursor.fetchone()[0]
        conn.commit()
        cursor.close()
        conn.close()
        return cliente_id
    
    def obtener_clientes(self):
        conn = self.conn_manager.get_connection()

        cursor = conn.cursor()
        cursor.execute("SELECT id, nombre, email, telefono FROM clientes")
        
        column_names = [desc[0] for desc in cursor.description]
        clientes = [dict(zip(column_names, row)) for row in cursor.fetchall()]
            
        cursor.close()
        conn.close()
        return clientes
    
    def actualizar_cliente(self, cliente_id: int, cliente: Cliente):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE clientes SET nombre = %s, email = %s, telefono = %s WHERE id = %s",
            (cliente.nombre, cliente.email, cliente.telefono, cliente_id)
        )
        updated_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return updated_rows > 0
    
    def eliminar_cliente(self, cliente_id: int):
        conn = self.conn_manager.get_connection()
        
        cursor = conn.cursor()
        cursor.execute("DELETE FROM clientes WHERE id = %s", (cliente_id,))
        deleted_rows = cursor.rowcount
        conn.commit()
        cursor.close()
        conn.close()
        return deleted_rows > 0
