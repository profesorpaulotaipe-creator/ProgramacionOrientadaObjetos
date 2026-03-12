import subprocess
import time
import sys
import os

def run():
    #Rutas de tus archivos
    api_path = os.path.join("api", "app.py")
    app_path = os.path.join("CrudClientesProductoVentas", "main.py")

    print("Iniciando API Flask....")
    api_process = subprocess.Popen([sys.executable, api_path])

    #Esperando para que la API se levante (Servidor BackEnd)
    time.sleep(2)

    print("Iniciando aplicacion de consola....")
    app_process = subprocess.Popen([sys.executable, app_path])
    
    try:
        #Esparando a que la app de consola se ejecute
        app_process.wait()
    except KeyboardInterrupt:
        print("\nCerrando Aplicacion o proceso...")

    #Finaliza ambos proceso al salir
    api_process.terminate()
    app_process.terminate()

if __name__ == "__main__":
    run()