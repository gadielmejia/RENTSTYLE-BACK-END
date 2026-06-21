from flask import Blueprint, jsonify

home_bp = Blueprint('home', __name__, url_prefix='/')

@home_bp.route('', methods=['GET'])
def home():
    """Ruta de bienvenida"""
    return jsonify({
        "status": "success",
        "message": "Bienvenido a RentStyle API",
        "version": "1.0.0",
        "endpoints": {
            "usuarios": "/api/usuarios",
            "prendas": "/api/prendas",
            "reservas": "/api/reservas",
            "categorias": "/api/categorias",
            "inventario": "/api/inventario"
        }
    }), 200
