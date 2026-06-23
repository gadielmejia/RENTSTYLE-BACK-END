from flask import jsonify

def response_success(data=None, message="Success", status_code=200):
    """Respuesta exitosa estándar"""
    return jsonify({
        "status": "success",
        "message": message,
        "data": data
    }), status_code

def response_error(message="Error", status_code=400, errors=None):
    """Respuesta de error estándar"""
    return jsonify({
        "status": "error",
        "message": message,
        "errors": errors
    }), status_code

def serialize_model(model, exclude_fields=None):
    """Convierte un modelo SQLAlchemy a diccionario"""
    if exclude_fields is None:
        exclude_fields = []
    
    result = {}
    for column in model.__table__.columns:
        if column.name not in exclude_fields:
            value = getattr(model, column.name)
            # Convertir datetime a string
            if hasattr(value, 'isoformat'):
                result[column.name] = value.isoformat()
            else:
                result[column.name] = value
    return result

def serialize_models(models, exclude_fields=None):
    """Convierte una lista de modelos a lista de diccionarios"""
    return [serialize_model(model, exclude_fields) for model in models]
