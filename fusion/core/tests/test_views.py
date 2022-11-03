from django.test import TestCase
from django.test import Client
from django.urls import reverse_lazy
from core.views import IndexView


class IndexViewTest(TestCase):

    def setUp(self):
        self.form_data = {
            "name": "Henrique",
            "email": "henrique@gmail.com.br",
            "subject": "Assunto",
            "message": "Mensagem teste"
        }
        self.url = reverse_lazy('index')
        self.client = Client()
        return

    def test_form_valid(self):
        data = self.form_data
        request = self.client.post(self.url, data=data)
        self.assertEqual(request.status_code, 302)  # valid form, 302 = moved cause was redirected
        return

    def test_form_invalid(self):
        data = self.form_data
        del data["name"]  # make form invalid by removing essencial data
        del data["email"]  # make form invalid by removing essencial data
        request = self.client.post(self.url, data=data)
        self.assertEqual(request.status_code, 200)  # invalid form, 200 = ok (why? maybe bc it was not redirect)
        return