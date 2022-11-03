from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey(get_user_model(), verbose_name="Autor", on_delete=models.CASCADE)
    title = models.CharField('Titulo', max_length=100)
    text = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.title
