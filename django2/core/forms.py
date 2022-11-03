from django import forms
from django.core.mail.message import EmailMessage
from django.conf import settings
import json
from .models import Produto


class ContatoForm(forms.Form):
    #  não integra com banco
    nome = forms.CharField(label='Nome', max_length=100, min_length=5)
    email = forms.EmailField(label='E-mail', max_length=100)
    assunto = forms.CharField(label='Assunto', max_length=120)
    mensagem = forms.CharField(label='Mensagem', widget=forms.Textarea())

    def send_mail(self):
        nome = self.cleaned_data['nome']
        email = self.cleaned_data['email']
        assunto = self.cleaned_data['assunto']
        mensagem = self.cleaned_data['mensagem']

        mail = EmailMessage(
            subject=f"[{settings.APP_NAME}] - {assunto}",
            body=f"Mensagem de: '{nome}'. Email: {email},\n{'-'*30}\n{mensagem}\n{'-'*30}\n",
            from_email=settings.EMAIL_HOST_USER,
            reply_to=[email],
            to=[settings.DEFAULT_TO_EMAIL]
        )

        mail.send()
        return


class ProdutoModelForm(forms.ModelForm):

    class Meta:
        model = Produto
        fields = ('name', 'price', 'inventory', 'image')
