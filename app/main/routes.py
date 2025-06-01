from flask import render_template, flash, redirect, url_for, request
from app.main import bp
from app import data # Importar o módulo data
from .forms import ContactForm # Importar o formulário de contato

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = ContactForm()
    if request.method == 'POST':
        print("Recebida requisição POST para /index") # DEBUG
        if form.validate_on_submit(): 
            name = form.name.data
            email = form.email.data
            subject = form.subject.data
            message_body = form.message.data
            
            print(f"DADOS VALIDADOS: Nova mensagem de: {name} ({email})")
            print(f"DADOS VALIDADOS: Assunto: {subject}")
            print(f"DADOS VALIDADOS: Mensagem: {message_body}")
            
            flash('Sua mensagem foi enviada com sucesso! Entrarei em contato em breve.', 'success')
            return redirect(url_for('main.index', _anchor='contact'))
        else:
            # A validação falhou
            print(f"VALIDAÇÃO FALHOU. Erros: {form.errors}") # DEBUG
            # Iterar sobre os erros para dar flash em cada um ou uma mensagem genérica
            error_messages = []
            for field, errors in form.errors.items():
                for error in errors:
                    error_messages.append(f"{getattr(form, field).label.text}: {error}")
            if error_messages:
                flash("Por favor, corrija os seguintes erros: " + "; ".join(error_messages), 'danger')
            else:
                flash('Ocorreu um erro de validação. Verifique os campos.', 'danger')
            # Não há redirect aqui, então o render_template abaixo será chamado,
            # passando o formulário com os erros para o template.
        
    return render_template('index.html', projects=data.PROJECTS, form=form)

# Rota dedicada para submit_contact_form não é mais estritamente necessária
# se o formulário for processado dentro da rota index.
# No entanto, vamos mantê-la por enquanto, caso queiramos separar a lógica
# ou se o CSRF/WTForms tiver problemas com o action="#" no template.
# A melhor prática seria ter o action apontando para url_for('main.index') ou uma rota específica.

@bp.route('/contact/submit', methods=['POST'])
def submit_contact_form():
    # Esta rota provavelmente não será usada se o formulário principal postar para main.index
    # Mas se for, ela deve ter uma lógica similar à acima ou simplesmente redirecionar.
    flash('A rota /contact/submit foi chamada, o que pode não ser o esperado.', 'info')
    return redirect(url_for('main.index', _anchor='contact'))

# A rota 'hello' pode ser removida se não estiver em uso.
# @bp.route('/hello')
# def hello():
# return 'Olá do Blueprint Main!'

# Adicionaremos mais rotas aqui para as seções do portfólio
# ex: /about, /projects, /contact 