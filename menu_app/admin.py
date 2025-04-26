"""
menu_app/admin.py
"""

from django.contrib import admin

# Register your models here.
from menu_app.models import MenuLinksModel, MenuModel, PageModel


class Menulinksinline(admin.TabularInline):
    """
    This is the list menu levels  for page from admin page. It is in \
the inside page, what containes the page description
    """
    model = MenuLinksModel
    extra = 1


class PageAdmin(admin.ModelAdmin):
    """
    This is the list of pages for interfaces from admin page
    """
    list_display = [
        "active",
        "template",
        "links",
        "text",
    ]  # ['title','menu_id','menu_parent','order','level']
    list_filter = [
        "active",
    ]
    inlines = [Menulinksinline]


class MenuAdmin(admin.ModelAdmin):
    """
    Menu admin to the interfaces from admin page
    """
    list_display = [
        "level",
    ]


admin.site.register(PageModel, PageAdmin)
admin.site.register(MenuModel, MenuAdmin)
