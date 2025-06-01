from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class ContactForm(FlaskForm):
    name = StringField(
        'Nome',
        validators=[
            DataRequired(message="Por favor, informe seu nome."),
            Length(min=2, max=100, message="O nome deve ter entre 2 e 100 caracteres.")
        ]
    )
    email = StringField(
        'Email',
        validators=[
            DataRequired(message="Por favor, informe seu email."),
            Email(message="Por favor, insira um email válido."),
            Length(max=120, message="O email não deve exceder 120 caracteres.")
        ]
    )
    subject = StringField(
        'Assunto',
        validators=[
            DataRequired(message="Por favor, informe o assunto."),
            Length(min=3, max=200, message="O assunto deve ter entre 3 e 200 caracteres.")
        ]
    )
    message = TextAreaField(
        'Mensagem',
        validators=[
            DataRequired(message="Por favor, escreva sua mensagem."),
            Length(min=10, max=2000, message="A mensagem deve ter entre 10 e 2000 caracteres.")
        ]
    )
    submit = SubmitField('Enviar Mensagem') 