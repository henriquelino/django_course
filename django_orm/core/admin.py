from django.contrib import admin

# Register your models here.
from .models import Chassi, Carro, Montadora


@admin.register(Chassi)
class ChassiAdmin(admin.ModelAdmin):
    list_display = ('number', )


@admin.register(Carro)
class CarroAdmin(admin.ModelAdmin):
    list_display = (
        'chassi_num',
        'montadora',
        'model',
        'price',
        'get_motoristas',
    )

    def get_motoristas(self, obj: Carro):
        return ', '.join(
            [motorista.username for motorista in obj.motoristas.all()])

    get_motoristas.short_description = 'Motoristas'


@admin.register(Montadora)
class MontadoraAdmin(admin.ModelAdmin):
    list_display = ('name', )
