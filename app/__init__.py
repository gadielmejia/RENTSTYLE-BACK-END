from flask import Flask
from flask_migrate import Migrate
from app.config.settings import Config
from app.database.database import db

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    
    # Inicializar Migrate después de db.init_app
    migrate = Migrate(app, db)
    
    # Importar todos los modelos para que SQLAlchemy los reconozca
    from app.models import (
        Roles, Categoria, Usuarios, Prenda, Inventario,
        Reserva, Detalle_Reserva, Comprobante, Cita
    )
    
    # Registrar Blueprints
    from app.routes.home_bp import home_bp
    from app.routes.roles_bp import roles_bp
    from app.routes.usuarios_bp import usuarios_bp
    from app.routes.prendas_bp import prendas_bp
    from app.routes.reservas_bp import reservas_bp
    from app.routes.categorias_bp import categorias_bp
    from app.routes.inventario_bp import inventario_bp
    
    app.register_blueprint(home_bp)
    app.register_blueprint(roles_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(prendas_bp)
    app.register_blueprint(reservas_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(inventario_bp)
    
    return app
