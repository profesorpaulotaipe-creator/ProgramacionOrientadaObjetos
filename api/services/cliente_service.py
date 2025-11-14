from database.db import DatabaseApi
from models.cliente import Cliente

class ClienteService:

    def __init__(self):
        self.db = DatabaseApi()

    def listar(self):
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "select * from clientes"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas
    
    def crear(self, cliente: Cliente):
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = """INSERT INTO clientes(nombre, apellido, correo, telefono)
                values(%s, %s, %s, %s)"""
        valores = (cliente.nombre, cliente.apellido, cliente.correo, cliente.telefono)
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0
    
    def buscar_por_id(self, id_cliente):
        conn = self.db.conectar()
        id_cliente = int(id_cliente)
        cur = conn.cursor(dictionary=True)
        sql = "select * from clientes where id_cliente = %s"
        cur.execute(sql, (id_cliente,))
        fila = cur.fetchone()
        conn.close
        return fila
    
    def actualizar(self, cliente: Cliente):
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = """update clientes
        set nombre= %s, apellido= %s, correo=%s, telefono=%s
        where id_cliente=%s"""
        valores= (cliente.nombre, cliente.apellido,cliente.correo, cliente.telefono, cliente.id_cliente)
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.rowcount > 0
    
    def eliminar(self, id_cliente):
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "DELETE from clientes where id_cliente = %s"
        cur.execute(sql, (id_cliente,))
        conn.commit()
        conn.close()
        return cur.rowcount > 0