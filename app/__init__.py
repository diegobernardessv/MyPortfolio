# app/__init__.py

from flask import Flask
from datetime import datetime
from .config import config_by_name

# Função utilitária para formatar data no Jinja2
def format_datetime(value, fmt='%Y-%m-%d %H:%M'):
    if isinstance(value, str) and value == "now":
        value = datetime.utcnow()
    if not isinstance(value, datetime):
        return value # Retorna o valor original se não for datetime
    return value.strftime(fmt)

def create_app(config_name):
    app = Flask(__name__, instance_relative_config=True)
    
    # Carrega a configuração do objeto
    config_obj = config_by_name.get(config_name)
    app.config.from_object(config_obj)

    # Armazena o nome do ambiente para uso posterior, por exemplo, nos templates
    app.config['FLASK_CONFIG'] = config_name

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