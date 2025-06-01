# app/__init__.py

from flask import Flask
from datetime import datetime

# Função utilitária para formatar data no Jinja2
def format_datetime(value, fmt='%Y-%m-%d %H:%M'):
    if isinstance(value, str) and value == "now":
        value = datetime.utcnow()
    if not isinstance(value, datetime):
        return value # Retorna o valor original se não for datetime
    return value.strftime(fmt)

def create_app(config_class_object):
    app = Flask(__name__, instance_relative_config=True)
    # Passar o objeto da classe de configuração diretamente
    app.config.from_object(config_class_object) 
    app.config.from_pyfile('config.py', silent=True) # Para carregar de instance/config.py

    # Registrar filtros Jinja2 customizados
    app.jinja_env.filters['datetimeformat'] = format_datetime

    # Inicializar extensões Flask (ex: db, migrate, mail) aqui, se necessário

    # Registrar Blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)

    # Adicionar uma rota de teste simples
    @app.route('/hello')
    def hello():
        return 'Hello, World from Portfolio App!'

    return app 