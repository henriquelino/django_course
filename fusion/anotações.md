Criar projeto com `django-admin startproject <nome> .` . para criar na mesma pasta
para criar um app: `django-admin createapp <nome>`

Rodar servidor com `python manage.py runserver`


nos templates usar: `{% load i18n %}`; e nos textos: `{% trans '<texto aqui>' %}`
nos forms e models: `from django.utils.translation import gettext_lazy as _`
nas views: `from django.utils.translation import gettext as _`
depois usar: `_('<texto_que_sera_traduzido>')`
Para atualizar arquivo po (arquivo de traduções) usar `python manage.py makemessages -l <lingua>` (es para espanhol, por exemplo)
Após atualizar arquivo po na pasta locale, usar `python manage.py compilemessages`
