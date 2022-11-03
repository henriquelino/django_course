from django.db import models
from stdimage.models import StdImageField

# SIGNALS
from django.db.models import signals
from django.template.defaultfilters import slugify

# Create your models here.


class Base(models.Model):
    created = models.DateField('Data de criação', auto_now_add=True)
    modified = models.DateField('Data de modificação', auto_now=True)
    active = models.BooleanField('Ativo?', default=True)

    class Meta:
        abstract = True  # não é criada em banco


class Produto(Base):
    name = models.CharField('Nome', max_length=100)
    price = models.DecimalField('Preço', max_digits=9, decimal_places=2)
    inventory = models.IntegerField('Estoque')
    image = StdImageField('Imagem', upload_to='produtos', variations={'thumb': (124, 124)})
    slug = models.SlugField('Slug', max_length=100, blank=True, editable=False)

    def __str__(self):
        return self.name

    @classmethod
    def pre_save(cls, signal, instance, sender, **kwargs):
        print(f"{cls}")
        print(f"{signal}")
        print(f"{instance}")
        print(f"{sender}")
        print(f"{kwargs = }")
        instance.slug = slugify(instance.name)


signals.pre_save.connect(Produto.pre_save, sender=Produto)
