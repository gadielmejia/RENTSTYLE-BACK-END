from flask import Blueprint, request
from app.database.database import db
from app.models.inventario import Inventario
from app.models.prenda import Prenda
from app.utils.response import response_success, response_error, serialize_model, serialize_models

inventario_bp = Blueprint('inventario', __name__, url_prefix='/api/inventario')

# GET - Obtener todo el inventario
@inventario_bp.route('', methods=['GET'])
def get_inventario():
    try:
        items = Inventario.query.all()
        return response_success(serialize_models(items), "Inventario obtenido exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# GET - Obtener item por ID
@inventario_bp.route('/<int:id>', methods=['GET'])
def get_item_inventario(id):
    try:
        item = Inventario.query.get(id)
        if not item:
            return response_error("Item no encontrado", 404)
        return response_success(serialize_model(item), "Item obtenido exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# GET - Obtener items por estado
@inventario_bp.route('/estado/<estado>', methods=['GET'])
def get_items_by_estado(estado):
    try:
        items = Inventario.query.filter_by(estado=estado).all()
        if not items:
            return response_error(f"No hay items con estado '{estado}'", 404)
        return response_success(serialize_models(items), "Items obtenidos exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# POST - Agregar item al inventario
@inventario_bp.route('', methods=['POST'])
def create_item_inventario():
    try:
        data = request.get_json()
        
        if not data:
            return response_error("El body debe ser un JSON válido", 400)
        
        # Validar campos requeridos
        required_fields = ['idPrenda', 'codigo_interno']
        for field in required_fields:
            if field not in data:
                return response_error(f"El campo '{field}' es requerido", 400)
        
        # Verificar que la prenda existe
        if not Prenda.query.get(data['idPrenda']):
            return response_error("La prenda especificada no existe", 400)
        
        # Verificar que el código interno es único
        if Inventario.query.filter_by(codigo_interno=data['codigo_interno']).first():
            return response_error("El código interno ya existe", 400)
        
        item = Inventario(
            idPrenda=data['idPrenda'],
            codigo_interno=data['codigo_interno'],
            estado=data.get('estado', 'Disponible')
        )
        item.save()
        
        return response_success(serialize_model(item), "Item agregado exitosamente", 201)
    except Exception as e:
        return response_error(str(e), 500)

# PUT - Actualizar estado del inventario
@inventario_bp.route('/<int:id>', methods=['PUT'])
def update_item_inventario(id):
    try:
        item = Inventario.query.get(id)
        if not item:
            return response_error("Item no encontrado", 404)
        
        data = request.get_json()
        
        if not data:
            return response_error("El body debe ser un JSON válido", 400)
        
        if 'estado' in data:
            valid_states = ['Disponible', 'Reservado', 'Alquilado', 'Reparacion']
            if data['estado'] not in valid_states:
                return response_error(f"Estado inválido. Estados válidos: {', '.join(valid_states)}", 400)
            item.estado = data['estado']
        
        item.save()
        
        return response_success(serialize_model(item), "Item actualizado exitosamente")
    except Exception as e:
        return response_error(str(e), 500)

# DELETE - Eliminar item del inventario
@inventario_bp.route('/<int:id>', methods=['DELETE'])
def delete_item_inventario(id):
    try:
        item = Inventario.query.get(id)
        if not item:
            return response_error("Item no encontrado", 404)
        
        item.delete()
        
        return response_success(message="Item eliminado exitosamente")
    except Exception as e:
        return response_error(str(e), 500)
