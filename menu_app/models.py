"""'
menu_app/models.py
"""

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class CustomUser(AbstractUser):
    groups = models.ManyToManyField(
        "auth.Group",
        related_name="%(class)s_groups",
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions "
            "granted to each of their groups."
        ),
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="%(class)s_user_permissions",
        # Уникальное имя для обратной связи
        blank=True,
        help_text=_("Specific permissions for this user."),
        verbose_name="user permissions",
    )
