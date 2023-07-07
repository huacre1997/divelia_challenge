from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    class Departments(models.TextChoices):
        DEVELOPMENT = "development", _("Desarrollo")
        DESIGN = "design", _("Diseño")
        sales = "sales", _("Ventas")

    department = models.CharField(
        max_length=12,
        null=True,
        blank=True,
        choices=Departments.choices,
        verbose_name=_("Área"),
    )
    email = models.EmailField(_("Email"), unique=True)
    username = None

    REQUIRED_FIELDS = []

    USERNAME_FIELD = "email"

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name
