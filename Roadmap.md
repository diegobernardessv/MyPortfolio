# Roadmap do Projeto: Portfólio Pessoal Dinâmico

## Visão Geral
Desenvolver um portfólio pessoal interativo e moderno, para apresentação de projetos. O portfólio será construído com Python (Flask), HTML, CSS (Bootstrap 5) e JavaScript (ES6+), com foco em componentes reutilizáveis, animações e facilidade de atualização das informações.

## Stack Tecnológico
- **Backend**: Python (Flask)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript (ES6+)
- **Banco de Dados**: PostgreSQL
- **Hospedagem**: Docker + Kubernetes
- **Versionamento**: Git

## Fases do Projeto

### Fase 1: Estrutura Base, Design Inicial e Seções Essenciais (MVP)
1.  **Configuração do Ambiente de Desenvolvimento:**
    *   [X] Criar estrutura de pastas do projeto Flask (`app`, `static`, `templates`, `instance` para configurações).
    *   [X] Configuração inicial do Flask (`__init__.py` com app factory, `config.py`).
    *   [X] Criação de Blueprints básicos (ex: `main` para rotas do portfólio).
    *   [X] Inclusão do Bootstrap 5 e um arquivo CSS customizado (`static/css/style.css`).
    *   [X] Criação do `requirements.txt` (Flask, etc.).
    *   [X] Configuração do `Dockerfile` e `docker-compose.yml` (recomendado para consistência).
2.  **Criação e Refinamento do `Roadmap.md` (este documento).**
    *   [X] Versão inicial criada.
    *   [X] Revisar e detalhar com base no feedback do usuário.
3.  **Layout Principal e Navegação:**
    *   [X] Criar template base (`templates/base.html`) com Jinja2 (estrutura HTML, inclusão de CSS/JS, blocos para header, content, footer).
    *   [X] Implementar a barra de navegação fixa no topo (`templates/partials/_navbar.html`), inspirada na referência, com links para as futuras seções.
    *   [X] Estilização inicial global e da navegação.
4.  **Seção Home/Hero:**
    *   [X] Estrutura HTML (`templates/partials/_home.html`).
    *   [X] Conteúdo: Nome, título/profissão.
    *   [X] Implementar efeito de digitação em JavaScript para o título/subtítulo.
    *   [X] Botões de CTA (ex: "Meus Projetos", "Contato").
    *   [X] Links para redes sociais (ícones).
5.  **Seção Sobre Mim (About):**
    *   [X] Estrutura HTML (`templates/partials/_about.html`).
    *   [X] Layout para foto e texto descritivo.
    *   [X] Campos para informações chave.
6.  **Seção Habilidades (Skills):**
    *   [X] Estrutura HTML (`templates/partials/_skills.html`).
    *   [X] Exibição de habilidades (ex: ícones + texto, agrupados por categoria).
    *   [ ] Considerar interatividade com JS (ex: animação ao rolar para a seção).
7.  **Rodapé (Footer):**
    *   [X] Estrutura HTML (`templates/partials/_footer.html`).
    *   [X] Links para redes sociais, copyright.
8.  **Dados Iniciais:**
    *   [X] Criar um arquivo (ex: `data.py` ou `data.json`) para armazenar os textos, links, listas de habilidades e informações dos projetos, facilitando a alteração.

### Fase 2: Conteúdo Interativo e Seções Adicionais
1.  **Seção Projetos (Portfolio/Work):**
    *   [X] Estrutura HTML (`templates/partials/_projects.html`).
    *   [X] Design de cards para projetos (imagem, título, descrição, tecnologias, links GitHub/Live).
    *   [X] Carregar dados dos projetos do arquivo `data.py/json`.
    *   [X] Efeitos de hover/animações com JavaScript nos cards.
    *   [X] (Opcional) Modal para detalhes do projeto.
    *   [X] (Opcional) Filtros para projetos (por tecnologia, tipo).
2.  **Seção Contato (Contact):**
    *   [X] Estrutura HTML (`templates/partials/_contact.html`).
    *   [X] Formulário de contato (HTML inicial, backend do formulário será Fase 3).
    *   [X] Exibir informações de contato (email, LinkedIn, etc.).
3.  **JavaScript Geral e Interatividade:**
    *   [X] Scroll Suave para links internos da navegação.
    *   [X] "Scroll Spy" para destacar a seção ativa na navegação.
    *   [X] Animações sutis em elementos ao rolar a página (efeito "reveal").
    *   [X] Garantir responsividade completa com Bootstrap e ajustes customizados.

### Fase 3: Funcionalidades Avançadas, Backend e Polimento
1.  **Backend do Formulário de Contato:**
    *   [X] Rota Flask para receber os dados do formulário.
    *   [X] Validação dos dados.
    *   [X] Envio de email (ex: usando Flask-Mail) ou armazenamento da mensagem.
2.  **Tema Claro/Escuro (Dark Mode):**
    *   [X] Implementar a lógica de alternância de tema com JavaScript.
    *   [X] Definir paletas de cores para ambos os temas.
    *   [X] Salvar a preferência do usuário (localStorage).
3.  **Otimizações:**
    *   [X] Otimização de imagens.
    *   [X] Minificação de CSS/JS para produção.
    *   [X] Revisão de performance.
4.  **Acessibilidade (WCAG):**
    *   [X] Revisar o site para garantir boas práticas de acessibilidade (contraste, navegação por teclado, ARIA labels onde necessário).
5.  **SEO Básico:**
    *   [X] Meta tags (título, descrição, keywords) para cada página/seção principal.
    *   [X] `robots.txt` e `sitemap.xml` (pode ser gerado dinamicamente ou estático).
6.  **"Download CV":**
    *   [X] Adicionar botão e funcionalidade para download do CV (arquivo PDF na pasta `static`).

### Fase 4: Testes e Deploy
1.  **Testes Finais:**
    *   [ ] Testes de usabilidade em diferentes dispositivos e navegadores.
    *   [ ] Verificar todos os links e funcionalidades.
2.  **Escolha da Plataforma de Hospedagem e Deploy:**
    *   [ ] Configurar o ambiente de produção.
    *   [ ] Realizar o deploy da aplicação Flask.
    *   [ ] Configurar domínio customizado e SSL.

## Considerações Adicionais
- **JavaScript:** Conforme solicitado, o JavaScript será amplamente utilizado para interatividade, animações, manipulação do DOM e criação de uma experiência de usuário fluida e moderna, inspirada no site de referência.
- **Facilidade de Alteração de Informações:** Os dados principais do portfólio (textos, informações de projetos, habilidades, etc.) serão gerenciados centralizadamente (provavelmente em um arquivo Python ou JSON dedicado no início) para permitir modificações rápidas sem necessidade de alterar diretamente o HTML ou a lógica complexa.
- **Componentes Reutilizáveis:** Em Flask/Jinja2, usaremos `macros` e `include` para criar componentes de template reutilizáveis (ex: card de projeto, item de habilidade). No JavaScript, funções e classes serão organizadas para promover a reutilização.
- **Seção Experiência:** Foco inicial nos projetos. A seção "Experiência" pode ser considerada para adição futura, se desejado.

## Próximos Passos (Imediatos)
-   [X] Discutir e validar esta versão do Roadmap com o usuário.
-   [X] Iniciar a Fase 1, começando pela configuração do ambiente de desenvolvimento e estrutura básica do Flask.

---

Este `Roadmap.md` será um documento vivo, atualizado após a conclusão e aprovação de cada funcionalidade ou etapa significativa. 