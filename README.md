# Portfólio Diego Bernardes Silva - Desenvolvedor Full Stack

Este é o repositório do meu portfólio pessoal, uma aplicação web dinâmica desenvolvida para apresentar meus projetos, habilidades e informações de contato de uma forma moderna e interativa.

## Tecnologias Utilizadas

*   **Backend:** Python com Flask
*   **Frontend:** HTML5, CSS3, JavaScript (ES6+)
*   **Framework CSS:** Bootstrap 5
*   **Templating:** Jinja2
*   **Gerenciamento de Formulários:** Flask-WTF
*   **Banco de Dados (Potencial Futuro):** PostgreSQL (planejado, com Alembic para migrações)

## Configuração e Execução Local

Siga os passos abaixo para configurar e executar o projeto em seu ambiente local:

1.  **Clone o repositório (se ainda não o fez):**
    ```bash
    git clone <URL_DO_SEU_REPOSITORIO_AQUI>
    cd DB_Portfolio
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Para Windows
    python -m venv .venv
    .venv\Scripts\activate

    # Para macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as variáveis de ambiente (se necessário):**
    Crie um arquivo `.env` na raiz do projeto se houver configurações específicas, como `SECRET_KEY` (embora para desenvolvimento, a `SECRET_KEY` no `config.py` possa ser suficiente). O `config.py` já deve ter uma `SECRET_KEY` definida.

5.  **Execute a aplicação Flask:**
    ```bash
    python main.py
    ```
    A aplicação estará disponível em `http://127.0.0.1:5000/`.

## Estrutura do Projeto

A estrutura principal do projeto é organizada da seguinte forma:

```
DB_Portfolio/
├── app/                    # Contém o core da aplicação Flask
│   ├── __init__.py         # Fábrica da aplicação (create_app)
│   ├── config.py           # Configurações da aplicação
│   ├── data.py             # Dados estáticos (ex: projetos)
│   ├── main/               # Blueprint principal (rotas, formulários)
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── static/             # Arquivos estáticos (CSS, JS, imagens)
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   └── templates/          # Templates HTML (Jinja2)
│       ├── partials/       # Fragmentos de templates reutilizáveis
│       ├── base.html       # Layout base
│       └── index.html      # Página principal
├── instance/               # Arquivos de instância (ex: banco de dados SQLite, se usado)
├── .venv/                  # Ambiente virtual Python
├── main.py                 # Ponto de entrada para executar a aplicação
├── requirements.txt        # Dependências Python do projeto
├── Roadmap.md              # Planejamento e fases do projeto
└── README.md               # Este arquivo
```

## Contato

Para entrar em contato, utilize o formulário na seção "Contato" da aplicação ou envie um email para diegobernardessv@gmail.com.

---
