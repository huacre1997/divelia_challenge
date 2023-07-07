from django.db import models
from django.utils.translation import gettext_lazy as _


class ModelBase(models.Model):
    is_active = models.BooleanField(default=True, verbose_name=_("Activo"))

    class Meta:
        abstract = True
