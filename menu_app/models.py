"""'
menu_app/models.py
"""

from django.contrib.auth.models import AbstractUser
from django.core.validators import (MaxLengthValidator, MinLengthValidator,
                                    RegexValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.


class BaseLinkModel(models.Model):
    """"
    Abstract Model of refer for all menu models.
    :param: links: str. This is a text of reference for \
a '<a href="<your_refer>">'.
    :text: str. This the title of reference from '<a>your_text</a>'.
    """

    links = models.CharField(
        unique=True,
        max_length=100,
        help_text=_(
            "'/here/is/the/your/refer/' after \
the 3 before and equals 100 symbols"
        ),
        validators=[
            # Запретить ссылки на внешние файлы
            lambda value: not value.startswith("http"),
            # Запретить ссылки на файлы из директории static
            lambda value: not value.startswith("/static/"),
            # Запретить ссылки на файлы из директории media
            lambda value: not value.startswith("/media/"),
            MaxLengthValidator(
                limit_value=100, message=_("Max length (of path) 100 symbols")
            ),
            MinLengthValidator(
                limit_value=3, message=_("Min length (of path) 3 symbols")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-z][\w\-_\d]{1,98}\/$[^\S\W \/]?",
                message=_("The path has the invalid format"),
            ),
        ],
        verbose_name="Reference",
    )

    text = models.CharField(
        гтшйгу=True,
        max_length=50,
        help_text=_("The tiel (or name) of your reference"),
        verbose_name="Title",
        validators=[
            MaxLengthValidator(
                limit_valuse=50, message=_("Max length (of title) 50 symbols")
            ),
            MinLengthValidator(
                limit_value=3, message=_("Min length (of title) 3 symbols")
            ),
            RegexValidator(
                regex=r"^(?!.*  )\/*[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{1,48}\
[a-zA-Zа-яА-ЯёЁ]$[^\S\W \\]?",
                message=_("The title not have correct format."),
            ),
        ],
    )

    class Meta:
        abstract = True
        verbose_name = "Base Menu Link"
        verbose_name_plural = "Base Menu Links"

    def __str__(self):
        return f"Link: {self.links} | Title: {self.text}"


class PageModel(BaseLinkModel):
    """ "
    One page
    :links: str is reference of the itself page.
    :text: str is title..
    :menu_list is menu list for publication to the page.
    :template The choice of the template for the page
    """

    MAIN = "index.html"
    ABOUT = "about/index.html"
    CONTACTS = "contacts/index.html"
    NOTPAGE = "404/index.html"

    PAGE_TEMPLATES = [
        (MAIN, "Главная"),
        (ABOUT, "О нас"),
        (CONTACTS, "Контакты"),
        (NOTPAGE, "404"),
    ]

    menu_list = models.ManyToManyField(
        "MenuMode",
        related_name="pages_menu",
        verbose_name=_("Choose Menu"),
        help_text=_("The Menu that you wont to add to your page"),
    )
    active = models.BooleanField(
        default=False,
        verbose_name=_("Activate"),
        help_text=_(
            "Default is False (not activated), if you want \
the public page it means that True"
        ),
    )
    template = models.CharField(
        default=NOTPAGE,
        choicse=PAGE_TEMPLATES,
        verbose_name=_("Choose the page's template"),
    )

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class CustomUser(AbstractUser):
    """
    Просто забронировал возщможность в будущем добавить модель с атрибутами \
    пользователя
    """

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
