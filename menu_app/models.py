"""'
menu_app/models.py
"""
from django.contrib.auth.models import AbstractUser
from django.core.validators import (MaxLengthValidator, MinLengthValidator,
                                    RegexValidator)
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
from sqlalchemy import Boolean, Column , Integer, String as BaseString, ForeignKey
from sqlalchemy.orm import relationship, validates
from project.sqlalchemy_utils import BaseModel
from enum import Enum as PyEnum, Enum


class String(BaseString):
    def __init__(self, length=None, help_text=None, **kwargs ):
        super().__init__(length=length, **kwargs)
        self.help_text = help_text

# class Column(BaseColumn):
#     def __init__(self, *args,  verbose_name=None, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.verbose_name = verbose_name
        
        

class BaseLinkModel(BaseModel):
    """"
    Abstract Model of refer for all menu models.
    :param: links: str. This is a text of reference for \
a '<a href="<your_refer>">'.
    :text: str. This the title of reference from '<a>your_text</a>'.
    """
    __tablename__ = "BaseLinkModel"
    id = Column(Integer, primary_key=True, index=True)
    Links = Column(String(100, help_text=_(
            "'/here/is/the/your/refer/' after \
the 1 before and equals 100 symbols")),
                   nullable=False, unique=False,
                   info={"verbose_name": "Reference"})
        
    text = Column(String(50,
                        help_text=_("The tiel (or name) of your reference")),
                 nullable=False, unique=False,
                 info={"verbose_name": "Title"},)

    
    @validates("links")
    def validate_links(self, key, links):
        # check the minim-length
        if len(links) < 1:
            raise ValueError("Min length (of path) is 100 symbols")
        
        # check the maxsim length
        if len(links) > 100:
            raise ValueError("Max length (of path) is 100 symbols")
        
        # Check the path url of format bu the regexp
        import re
        if not re.match(r'(\/||^(?!.*  )[a-z][\w\-_\d]{1,9}\/$[^\S\W ]',
                        links):
            raise ValueError(_("The path has the invalid format"))

class TemplateType(PyEnum):
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
    
class PageModel(BaseLinkModel):
    __tablename__ = 'PageModel'
    """
    One page
    :links: str is reference of the itself page.
    :text: str is title..
    :menu_list is menu list for publication to the page.
    :template The choice of the template for the page
    """
    id = Column(Integer, primary_key=True, index=True)
    active = Column(Boolean, default=False)
    template = Column(
        Enum(TemplateType),
        default=TemplateType.MAIN,
        info={
            'verbose_name': _("Choose the page's template"),
            'choices': [(t.value, t.name) for t in TemplateType],
        }
    )

class SubPageModel(PageModel):
    """
    Subpage of the PageModel
    """
    __tablename__ = 'SubPageModel'
    id = Column(Integer, primary_key=True, index=True)
    parent = Column(String, default="", null=True, blank=True)
    parent_page = Column(ForeignKey("PageModel.id", ondelete='CASCADE'))
    
class SubPageModel(PageModel):
    """
    Subpage of the PageModel
    """
    
    parent = models.CharField(default="", null=True, blank=True)
    parent_page = models.ForeignKey(
        PageModel, on_delete=models.CASCADE, related_name="subpages"
    )

    def save(self, *args, **kwargs):
        if not self.parent:
            self.parent = self.parent_page.text
        super().save(*args, **kwargs)


class levelMenuModel(models.TextChoices):
    """
    Level menu
    """
    TOP = "TOP", _("Верхний")
    SIDE = "SIDE", _("Боковой")
    BOTTOM = "BOTTOM", _("Нижний")
    PLUG = "PLUG", _("Заглушка")


class MenuModel(models.Model):
    """
    Menu for navigation
    :links: str is reference of the itself page.
    :text: str is title..
    :menu_list is menu list for publication to the page.
    :template The choice of the template for the page
    """
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


class MenuLinksModel(models.Model):
    """
    Модель связи между страницами и меню
    """
    pages = models.ForeignKey(
        PageModel, on_delete=models.CASCADE, related_name="linksPages"
    )
    menu = models.ForeignKey(
        MenuModel, on_delete=models.CASCADE, related_name="linksPages"
    )



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
