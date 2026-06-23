from flask import Blueprint, request
from app.database.database import db
from app.models.prenda import Prenda
from app.models.categoria import Categoria
from app.utils.response import response_success, response_error, serialize_model, serialize_models

prendas_bp = Blueprint('prendas', __name__, url_prefix='/api/prendas')

# GET - Obtener todas las prendas
@prendas_bp.route('', methods=['GET'])
def get_prendas():
    try:
        prendas = Prenda.query.all()
        return response_success(serialize_models(prendas), "Prendas obtenidas exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# GET - Obtener prenda por ID
@prendas_bp.route('/<int:id>', methods=['GET'])
def get_prenda(id):
    try:
        prenda = Prenda.query.get(id)
        if not prenda:
            return response_error("Prenda no encontrada", 404)
        return response_success(serialize_model(prenda), "Prenda obtenida exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# GET - Obtener prendas por categoría
@prendas_bp.route('/categoria/<int:id_categoria>', methods=['GET'])
def get_prendas_by_categoria(id_categoria):
    try:
        prendas = Prenda.query.filter_by(idCategoria=id_categoria).all()
        if not prendas:
            return response_error("No hay prendas en esta categoría", 404)
        return response_success(serialize_models(prendas), "Prendas obtenidas exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# POST - Crear nueva prenda
@prendas_bp.route('', methods=['POST'])
def create_prenda():
    try:
        data = request.get_json()
        
        if not data:
            return response_error("El body debe ser un JSON válido", 400)
        
        # Validar campos requeridos
        required_fields = ['nombre_prenda', 'idCategoria', 'precio_alquiler']
        for field in required_fields:
            if field not in data:
                return response_error(f"El campo '{field}' es requerido", 400)
        
        # Verificar que la categoría existe
        if not Categoria.query.get(data['idCategoria']):
            return response_error("La categoría especificada no existe", 400)
        
        prenda = Prenda(
            nombre_prenda=data['nombre_prenda'],
            idCategoria=data['idCategoria'],
            descripcion=data.get('descripcion'),
            talla=data.get('talla'),
            color=data.get('color'),
            precio_alquiler=data['precio_alquiler']
        )
        prenda.save()
        
        return response_success(serialize_model(prenda), "Prenda creada exitosamente", 201)
    except Exception as e:
        return response_error(str(e), 500)

# PUT - Actualizar prenda
@prendas_bp.route('/<int:id>', methods=['PUT'])
def update_prenda(id):
    try:
        prenda = Prenda.query.get(id)
        if not prenda:
            return response_error("Prenda no encontrada", 404)
        
        data = request.get_json()
        
        if not data:
            return response_error("El body debe ser un JSON válido", 400)
        
        # Actualizar solo los campos proporcionados
        if 'nombre_prenda' in data:
            prenda.nombre_prenda = data['nombre_prenda']
        if 'descripcion' in data:
            prenda.descripcion = data['descripcion']
        if 'talla' in data:
            prenda.talla = data['talla']
        if 'color' in data:
            prenda.color = data['color']
        if 'precio_alquiler' in data:
            prenda.precio_alquiler = data['precio_alquiler']
        if 'idCategoria' in data:
            if not Categoria.query.get(data['idCategoria']):
                return response_error("La categoría especificada no existe", 400)
            prenda.idCategoria = data['idCategoria']
        
        prenda.save()
        
        return response_success(serialize_model(prenda), "Prenda actualizada exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# DELETE - Eliminar prenda
@prendas_bp.route('/<int:id>', methods=['DELETE'])
def delete_prenda(id):
    try:
        prenda = Prenda.query.get(id)
        if not prenda:
            return response_error("Prenda no encontrada", 404)
        
        prenda.delete()
        
        return response_success(message="Prenda eliminada exitosamente")
    except Exception as e:
        return response_error(str(e), 500)
