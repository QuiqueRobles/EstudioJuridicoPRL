from flask import Flask

def create_app(config_name):
    app = Flask(__name__)
    
    # Importar el diccionario de configuración dentro de la función
    from .config import config
    app.config.from_object(config[config_name])

    # Importar rutas aquí
    with app.app_context():
        from . import routes

    return app
