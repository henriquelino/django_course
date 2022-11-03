from django.test import TestCase
from model_mommy import mommy

from core.forms import ContactForm


class ContactFormTestCase(TestCase):

    def setUp(self):
        self.form_data = {
            "name": "Henrique",
            "email": "henrique@teste.email.com.br",
            "subject": "Assunto",
            "message": "Mensagem teste",
        }
        self.form = ContactForm(data=self.form_data)
        return

    def test_send_mail(self):
        self.form.is_valid()  # carrega os dados do formulário e faz as validações
        r = self.form.send_email()
        self.assertEqual(r, 1)
        return
