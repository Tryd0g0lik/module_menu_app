# Generated by Django 4.2.17 on 2025-04-26 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu_app', '0016_subpagemodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='subpagemodel',
            name='parent',
            field=models.CharField(default=models.F('text')),
        ),
    ]
