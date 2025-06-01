# app/config.py

import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'uma-chave-secreta-muito-dificil-de-adivinhar'
    # Outras configurações globais da aplicação

class DevelopmentConfig(Config):
    DEBUG = True
    # Configurações específicas de desenvolvimento

class TestingConfig(Config):
    TESTING = True
    # Configurações específicas de teste

class ProductionConfig(Config):
    # Configurações específicas de produção
    # Ex: SECRET_KEY deve ser carregado de uma variável de ambiente segura
    # DEBUG = False
    # TESTING = False
    pass

# Mapeamento para facilitar a seleção da configuração
config_by_name = dict(
    development=DevelopmentConfig,
    testing=TestingConfig,
    production=ProductionConfig,
    default=DevelopmentConfig
) 