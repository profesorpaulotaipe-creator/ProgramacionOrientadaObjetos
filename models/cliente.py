class Cliente:
    
    def __init__(self, id_cliente=None, nombre="",apellido="", correo="", telefono=""):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.apellido = apellido
        self.correo = correo
        self.telefono = telefono