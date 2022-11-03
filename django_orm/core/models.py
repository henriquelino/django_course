from django.db import models
from django.contrib.auth import get_user_model


# Create your models here.
class Chassi(models.Model):
    number = models.CharField('Chassi', max_length=16)

    class Meta:
        verbose_name = 'Chasse'
        verbose_name_plural = 'Chassis'

    def __str__(self):
        return self.number


class Montadora(models.Model):
    name = models.CharField('Nome', max_length=50)

    class Meta:
        verbose_name = 'Montadora'
        verbose_name_plural = 'Montadoras'

    def __str__(self):
        return self.nome


def set_default_montadora():
    return Montadora.objects.get_or_create(nome='Padrão')[
        0]  # 0 is object, 1 is bool (true=created new, false=already exists)


class Carro(models.Model):
    """
    # OneToOne
    cada carro só pode ter 1 chassi
    e cada chassi só pode ter 1 carro

    # ForeignKey (One to many)
    Cada carro tem uma montadora
    mas cada montadora tem N carros

    # many to many
    Um carro pode ser dirigido por vários motoristas
    """
    chassi_num = models.OneToOneField(
        Chassi,
        on_delete=models.CASCADE)  # when deleting chassi, delete car too

    # when deleting montadora, delete car too, the common one to use
    montadora = models.ForeignKey(Montadora, on_delete=models.CASCADE)

    # when deleting montadora, car will get default montadora id as 1
    # montadora = models.ForeignKey(Montadora, on_delete=models.SET_DEFAULT, default=1)

    # when deleting montadora, car will get the return of function set_default_montadora
    # montadora = models.ForeignKey(Montadora, on_delete=models.SET(set_default_montadora))

    motoristas = models.ManyToManyField(get_user_model())
    model = models.CharField('Model', max_length=30)
    price = models.DecimalField('Price', max_digits=9, decimal_places=2)

    def __str__(self):
        return f"{self.montadora} {self.model}"
