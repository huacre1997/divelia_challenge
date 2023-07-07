from django.db import models
from apps.users.models import CustomUser
from django.utils.translation import gettext_lazy as _
from utils.models.base import ModelBase


class Pet(ModelBase):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name=_("Nombre"))
    image = models.ImageField(
        upload_to="pets/", null=True, blank=True, verbose_name=_("Foto"))
    short_name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name=_("Nombre corto"))
    owner = models.ForeignKey(
        CustomUser, null=False, blank=False, on_delete=models.PROTECT, verbose_name=_("Dueño"))

    def __str__(self):
        return self.short_name

    class Meta:
        verbose_name = _("Mascota")
        verbose_name_plural = _("Mascotas")
