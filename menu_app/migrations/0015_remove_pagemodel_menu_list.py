# Generated by Django 4.2.17 on 2025-04-26 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menu_app", "0014_menulinksmodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pagemodel",
            name="menu_list",
        ),
    ]
