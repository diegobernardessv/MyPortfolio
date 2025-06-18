# Fase 1: Build do ambiente
FROM python:3.11-slim as builder

WORKDIR /app

# Instalar dependências de build, se necessário
# RUN apt-get update && apt-get install -y ...

# Copiar requirements e instalar pacotes Python
COPY requirements.txt .
RUN pip wheel --no-cache-dir --no-deps --wheel-dir /app/wheels -r requirements.txt


# Fase 2: Imagem final de produção
FROM python:3.11-slim

WORKDIR /app

# Variáveis de ambiente
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP=main.py
ENV FLASK_CONFIG=production
ENV FLASK_ENV=production

# Copiar os pacotes pré-compilados da fase de build
COPY --from=builder /app/wheels /wheels
COPY --from=builder /app/requirements.txt .
RUN pip install --no-cache /wheels/*

# Copiar o código da aplicação
COPY . .

# Expor a porta que o Gunicorn vai usar
EXPOSE 5000

# Comando para iniciar a aplicação
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "main:app"] 