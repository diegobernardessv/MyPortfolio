# main.py

import os
from app import create_app
from app.config import config_by_name

# Obtém a configuração do ambiente, default 'development'
config_name = os.getenv('FLASK_CONFIG') or 'default'
app = create_app(config_by_name[config_name])

if __name__ == '__main__':
    app.run(debug=app.config.get('DEBUG', True)) 