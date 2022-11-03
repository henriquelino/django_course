from django import forms
from django.core.mail.message import EmailMessage

from django.conf import settings
from django.utils.translation import gettext_lazy as _  # gettext_lazy for forms and models


class ContactForm(forms.Form):
    name = forms.CharField(label=_("Nome"), max_length=100)
    email = forms.EmailField(label=_("E-mail"), max_length=255)
    subject = forms.CharField(label=_("Assunto"), max_length=100)
    message = forms.CharField(label=_("Mensagem"), widget=forms.Textarea())

    def send_email(self):
        nome = self.cleaned_data['name']
        email = self.cleaned_data['email']
        subject = self.cleaned_data['subject']
        message = self.cleaned_data['message']

        body = f"{_('Nome:')} {nome}\n{_('E-mail:')} {email}\n\n{_('Assunto:')} '{subject}'\n{_('Mensagem:')} '{message}'"

        mail = EmailMessage(
            subject=f"[{settings.APP_NAME}] - {subject}",
            body=body,
            from_email=f"Contato Fusion <{settings.EMAIL_HOST_USER}>",
            to=[settings.DEFAULT_TO_EMAIL],
            reply_to=[email],
        )
        r = mail.send()
        return r