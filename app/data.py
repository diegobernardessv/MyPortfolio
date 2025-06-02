# app/data.py

# Dados dos Projetos
# Preencha com os detalhes dos seus projetos.
# - 'image': Caminho relativo a partir da pasta 'static/', ex: 'img/nome_da_imagem.jpg'
# - 'technologies': Uma lista de strings com as tecnologias usadas.
# - 'repo_link': URL para o repositório do projeto.
# - 'live_link': URL para a demonstração ao vivo (opcional, pode ser None).

PROJECTS = [
    {
        'id': 'romaneiosapp', # um identificador único para o projeto
        'title': 'RomaneiosApp',
        'description': 'Plataforma completa para gestão e automação de suprimentos. Inclui CRUD de romaneios, assinaturas digitais (canvas), gerenciamento de caixas, notificações em tempo real, controle de acesso (3 níveis), delegação de assinaturas e relatórios. Arquitetura com Flask, PostgreSQL, Docker, e frontend responsivo com Bootstrap.',
        'image': 'projects/Romaneiosapp/Romaneiosapp_logo.PNG',
        'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap', 'PostgreSQL' , 'Docker', 'Kubernetes', 'GitLab CI/CD'],
        'repo_link': 'projects/Romaneiosapp/README.pdf', # Substitua pelo link do seu repositório
        'live_link': 'https://romaneiosapp.gbtech.cloud/login',    # Substitua pelo link da demo se houver, ou deixe None
        'gallery_images': [
            'projects/Romaneiosapp/pictures/1.Login.PNG',
            'projects/Romaneiosapp/pictures/2.Home.PNG',
            'projects/Romaneiosapp/pictures/3.Criar_romaneio.PNG',
            'projects/Romaneiosapp/pictures/4.Gestão de caixas.PNG',
            'projects/Romaneiosapp/pictures/5.Visao_caixas.PNG',
            'projects/Romaneiosapp/pictures/6.Relatorio.PNG',
            'projects/Romaneiosapp/pictures/7.Cadastro_usuarios.PNG',
            'projects/Romaneiosapp/pictures/8.Delegar_assinatura.PNG',
            'projects/Romaneiosapp/pictures/9.Navbar.PNG',
            'projects/Romaneiosapp/pictures/10.Assinar_romaneio.PNG',
            'projects/Romaneiosapp/pictures/11.Romaneio_assinado.PNG',
            'projects/Romaneiosapp/pictures/Funcionalidades.PNG',
            'projects/Romaneiosapp/pictures/Tecnologias e Arquitetura do Sistema.PNG'
        ]
    },
    {
        'id': 'nonconformity', # um identificador único para o projeto
        'title': 'NonConformity',
        'description': 'Solução robusta para gestão de não conformidades (NCR) com CRUD completo, perfis de usuário e fluxo definido. Prioriza segurança (hashing, CSRF) e integração via API REST completa com documentação Swagger.',
        'image': 'projects/NonConformity/NonConformity_logo.PNG', # Substitua por ex: 'img/nonconformity.jpg'
        'technologies': ['Python', 'Flask', 'HTML', 'CSS', 'JavaScript', 'Bootstrap', 'PostgreSQL' , 'Docker', 'Kubernetes', 'GitLab CI/CD'], 
        'repo_link': 'projects/NonConformity/README.pdf', # Substitua pelo link do seu repositório
        'live_link': 'https://nonconformity.gbtech.cloud/auth/login?next=%2Findex',    # Substitua pelo link da demo se houver, ou deixe None
    },
    # Adicione mais dicionários de projetos aqui, seguindo a mesma estrutura.
    # Exemplo de um terceiro projeto:
    # {
    #     'id': 'meuoutroprojeto',
    #     'title': 'Meu Outro Projeto Incrível',
    #     'description': 'Descrição do meu outro projeto...',
    #     'image': 'img/placeholder_project.png',
    #     'technologies': ['JavaScript', 'HTML', 'CSS'],
    #     'repo_link': '#',
    #     'live_link': '#',
    # },
]

# Você também pode adicionar outros dados aqui no futuro, como:
# - Depoimentos (TESTIMONIALS)
# - Linha do tempo de carreira (CAREER_TIMELINE) 