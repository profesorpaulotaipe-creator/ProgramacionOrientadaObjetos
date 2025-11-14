from flask import Blueprint, request, jsonify # pip install flask
from services.cliente_service import ClienteService
from models.cliente import Cliente

cliente_api = Blueprint("cliente_api", __name__)
service = ClienteService()

@cliente_api.get("/clientes")
def listar():
    return jsonify(service.listar())

@cliente_api.post("/clientes")
def crear():
    data = request.json
    cliente = Cliente(
        nombre=data["nombre"],
        apellido=data["apellido"],
        correo=data["correo"],
        telefono=data["telefono"]
    )
    service.crear(cliente)
    return jsonify({"msg": "Cliente Creado con Exito."})

@cliente_api.get("/clientes/<int:id_cliente>")
def buscar(id_cliente):
    return jsonify(service.buscar_por_id(id_cliente))