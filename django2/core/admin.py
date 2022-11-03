from django.contrib import admin

# Register your models here.
from .models import Produto


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'inventory', 'slug', 'created', 'modified', 'active')
