from django.db import models

from django.utils.translation import gettext_lazy as _
from apps.pets.models import Pet
from utils.models.base import ModelBase


class Toy(ModelBase):
    name = models.CharField(max_length=50, null=False,
                            blank=False, verbose_name=_("Nombre"))
    price = models.DecimalField(
        decimal_places=2, max_digits=10, null=False, blank=False, verbose_name=_("Precio"))
    url = models.URLField(null=False, blank=False, verbose_name=_("URL"))

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _("Juguete")
        verbose_name_plural = _("Juguetes")


class Gift(ModelBase):
    toy = models.ForeignKey(Toy, on_delete=models.PROTECT,
                            verbose_name=_("Juguete"))
    pet = models.ForeignKey(Pet, on_delete=models.PROTECT,
                            verbose_name=_("Mascota"))
