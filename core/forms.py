from django import forms
from django.core.mail.message import EmailMessage


class ContatoForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    email = forms.CharField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        conteudo = f'Nome : {nome}\nE-mail: {email}\n Assunto: {assunto}\nMensagem:{mensagem}'

        mail = EmailMessage(
            subject='E-mail enviado pelo sistema django2',
            body=conteudo,
            from_email='contato@seudominio.com.br',
            to=['contato@seucontato.com.br', ],
            headers={'Reply-To': email}
        )

        mail.send()
