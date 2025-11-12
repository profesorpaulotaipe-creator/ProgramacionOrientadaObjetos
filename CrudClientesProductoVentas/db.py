import mysql.connector

class Database:
    def __init__(self):
        self.config = {
            "host":"138.255.103.114",
            "port":3306,
            "user":"inacodec_poo_seccion_c2",
            "password":"AQm}ZzpW0ovqyaZJ",
            "database":"inacodec_dataPracticaApis"
        }
    
    def conectar(self):
        try:
            conn = mysql.connector.connect(**self.config)
            return conn        
        except mysql.connector.Error as err:
            print(f"Error de conexion: {err}")
            return None