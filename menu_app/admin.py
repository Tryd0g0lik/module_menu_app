"""
menu_app/admin.py
"""

from django.contrib import admin

# Register your models here.
from menu_app.models import MenuModel, PageModel


class PageAdmin(admin.ModelAdmin):
    list_display = [
        "active",
        "template",
        "links",
        "text",
    ]  # ['title','menu_id','menu_parent','order','level']


class MenuAdmin(admin.ModelAdmin):
    list_display = [
        "level",
    ]


admin.site.register(PageModel, PageAdmin)
# admin.site.register(levelMenuModel, LevelMenuAdmin)
admin.site.register(MenuModel, MenuAdmin)
