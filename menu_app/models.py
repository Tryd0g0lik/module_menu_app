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
        unique=False,
        max_length=100,
        help_text=_(
            "'/here/is/the/your/refer/' after \
the 1 before and equals 100 symbols"
        ),
        validators=[
            MaxLengthValidator(
                limit_value=100, message=_("Max length (of path) 100 symbols")
            ),
            MinLengthValidator(
                limit_value=1, message=_("Min length (of path) 1 symbols")
            ),
            RegexValidator(
                regex=r"(\/||^(?!.*  )[a-z][\w\-_\d]{1,9}\/$[^\S\W ])",
                message=_("The path has the invalid format"),
            ),
        ],
        verbose_name="Reference",
    )

    text = models.CharField(
        unique=False,
        max_length=50,
        help_text=_("The tiel (or name) of your reference"),
        verbose_name="Title",
        validators=[
            MaxLengthValidator(
                limit_value=50, message=_("Max length (of title) 50 symbols")
            ),
            MinLengthValidator(
                limit_value=3, message=_("Min length (of title) 3 symbols")
            ),
            RegexValidator(
                regex=r"^(?!.*  )[a-zA-Zа-яА-ЯёЁ][\w \-_\dа-яА-ЯёЁ]{1,48}[a-zA-Zа-яА-ЯёЁ]$[^\S\W \\]?",
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
    """
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
    PROFILE = "profile/index.html"

    PAGE_TEMPLATES = [
        (MAIN, "Главная"),
        (ABOUT, "О нас"),
        (CONTACTS, "Контакты"),
        (PROFILE, "Профиль"),
        (NOTPAGE, "404"),
    ]

    menu_list = models.ManyToManyField(
        "MenuModel",
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
        choices=PAGE_TEMPLATES,
        verbose_name=_("Choose the page's template"),
    )

    def __str__(self):
        return "%s" % self.text

    class Meta:
        verbose_name = "Page"
        verbose_name_plural = "Pages"


class levelMenuModel(models.TextChoices):
    TOP = "TOP", _("Верхний")
    SIDE = "SIDE", _("Боковой")
    BOTTOM = "BOTTOM", _("Нижний")


class MenuModel(models.Model):
    """
    Menu for navigation
    :links: str is reference of the itself page.
    :text: str is title..
    :menu_list is menu list for publication to the page.
    :template The choice of the template for the page
    """

    # page = models.ManyToManyField(
    #     PageModel,
    #     help_text=_("The path to the page's menu"),
    # ),
    level = models.CharField(
        default=levelMenuModel.TOP,
        choices=levelMenuModel.choices,
        verbose_name=_("Level manu"),
    )

    def __str__(self):
        return "%s" % (self.level)

    class Meta:
        verbose_name = _("Level of menu")
        verbose_name_plural = _("Levels of menu")


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
