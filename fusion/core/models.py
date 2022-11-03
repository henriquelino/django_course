import uuid

from django.db import models
from django.utils.translation import gettext_lazy as _  # gettext_lazy for forms and models
from stdimage.models import StdImageField


def get_file_path(__, filename: str):
    __, ext = filename.split('.')
    filename = f"{uuid.uuid4()}.{ext}"
    return filename


class Base(models.Model):
    created = models.DateField(_('Criado em'), auto_now_add=True)
    modified = models.DateField(_('Modificado em'), auto_now=True)
    active = models.BooleanField(_('Ativo?'), default=True)

    class Meta:
        abstract = True


class Service(Base):
    ICON_CHOICES = (
        ('lni-cog', 'cog'),
        ('lni-stats-up', 'graph'),
        ('lni-users', 'users'),
        ('lni-layers', 'design'),
        ('lni-mobile', 'mobile'),
        ('lni-rocket', 'rocket')
    ) # yapf: disable

    title = models.CharField(_("Service"), max_length=100)
    description = models.TextField(_("Description"), max_length=250)
    icon = models.CharField(_('Icon'), max_length=50, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Service')
        verbose_name_plural = _('Services')

    def __str__(self) -> str:
        return self.title


class Role(Base):
    role_name = models.CharField(_("role"), max_length=100)

    class Meta:
        verbose_name = _('Role')
        verbose_name_plural = _('Roles')

    def __str__(self) -> str:
        return f"{self.role_name}"


class TeamMember(Base):
    _thumb = {'thumb': {"width": 480, "height": 480, "crop": True}}

    name = models.CharField(_("Name"), max_length=100)
    role = models.ForeignKey('core.Role', verbose_name=_('Role'), on_delete=models.CASCADE)
    bio = models.CharField(_("Bio"), max_length=250)
    picture = StdImageField(_("Image"), upload_to=get_file_path, variations=_thumb, delete_orphans=True)

    facebook = models.CharField("Facebook", max_length=100, default='#')
    twitter = models.CharField("Twitter", max_length=100, default='#')
    instagram = models.CharField("Instagram", max_length=100, default='#')

    class Meta:
        verbose_name = _('Team member')
        verbose_name_plural = _('Team members')

    def __str__(self) -> str:
        return f"{self.name} - {self.role}"


class Feature(Base):
    ICON_CHOICES = (
        ('lni-rocket', 'rocket'),
        ('lni-laptop-phone', 'laptop'),
        ('lni-cog', 'cog'),
        ('lni-leaf', 'leaf'),
        ('lni-layers', 'layers')
    ) # yapf: disable

    name = models.CharField(_("Name"), max_length=100)
    description = models.TextField(_("Description"), max_length=250)
    icon = models.CharField(_('Icon'), max_length=50, choices=ICON_CHOICES)

    class Meta:
        verbose_name = _('Feature')
        verbose_name_plural = _('Features')

    def __str__(self) -> str:
        return self.name
