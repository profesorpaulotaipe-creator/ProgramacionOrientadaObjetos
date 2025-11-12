from db import Database
from models.producto import Producto

class ProductoService:
    
    def __init__(self):
        self.db = Database
    
    def listarProductos(self):
        conn = self.db.conectar()
        cur = conn.cursor(dictionary=True)
        sql = "select * from productos"
        cur.execute(sql)
        filas = cur.fetchall()
        conn.close()
        return filas

    def agregarProducto(self, producto: Producto):
        conn = self.db.conectar()
        cur = conn.cursor()
        sql = """insert into productos(imagen, nombre, descripcion, precio, stock, estado)
                values(%s,%s,%s,%s,%s,%s)"""
        valores = (producto.imagen, producto.nombre, producto.descripcion, producto.precio, producto.stock, producto.estado)
        cur.execute(sql, valores)
        conn.commit()
        conn.close()
        return cur.lastrowid