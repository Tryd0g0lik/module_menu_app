# Generated by Django 4.2.17 on 2025-04-25 07:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("menu_app", "0002_alter_menumodel_links_alter_menumodel_text_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="menumodel",
            name="links",
            field=models.CharField(
                help_text="'/here/is/the/your/refer/' after the 1 before and equals 100 symbols",
                max_length=100,
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        limit_value=100, message="Max length (of path) 100 symbols"
                    ),
                    django.core.validators.MinLengthValidator(
                        limit_value=1, message="Min length (of path) 1 symbols"
                    ),
                    django.core.validators.RegexValidator(
                        message="The path has the invalid format",
                        regex="^(?!.*  )[a-z][\\w\\-_\\d]{1,98}\\/$[^\\S\\W \\/]?",
                    ),
                ],
                verbose_name="Reference",
            ),
        ),
        migrations.AlterField(
            model_name="menumodel",
            name="text",
            field=models.CharField(
                help_text="The tiel (or name) of your reference",
                max_length=50,
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        limit_value=50, message="Max length (of title) 50 symbols"
                    ),
                    django.core.validators.MinLengthValidator(
                        limit_value=3, message="Min length (of title) 3 symbols"
                    ),
                    django.core.validators.RegexValidator(
                        message="The title not have correct format.",
                        regex="^(?!.*  )\\/*[a-zA-Zа-яА-ЯёЁ][\\w \\-_\\dа-яА-ЯёЁ]{1,48}[a-zA-Zа-яА-ЯёЁ]$[^\\S\\W \\\\]?",
                    ),
                ],
                verbose_name="Title",
            ),
        ),
        migrations.AlterField(
            model_name="pagemodel",
            name="links",
            field=models.CharField(
                help_text="'/here/is/the/your/refer/' after the 1 before and equals 100 symbols",
                max_length=100,
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        limit_value=100, message="Max length (of path) 100 symbols"
                    ),
                    django.core.validators.MinLengthValidator(
                        limit_value=1, message="Min length (of path) 1 symbols"
                    ),
                    django.core.validators.RegexValidator(
                        message="The path has the invalid format",
                        regex="^(?!.*  )[a-z][\\w\\-_\\d]{1,98}\\/$[^\\S\\W \\/]?",
                    ),
                ],
                verbose_name="Reference",
            ),
        ),
        migrations.AlterField(
            model_name="pagemodel",
            name="text",
            field=models.CharField(
                help_text="The tiel (or name) of your reference",
                max_length=50,
                unique=True,
                validators=[
                    django.core.validators.MaxLengthValidator(
                        limit_value=50, message="Max length (of title) 50 symbols"
                    ),
                    django.core.validators.MinLengthValidator(
                        limit_value=3, message="Min length (of title) 3 symbols"
                    ),
                    django.core.validators.RegexValidator(
                        message="The title not have correct format.",
                        regex="^(?!.*  )\\/*[a-zA-Zа-яА-ЯёЁ][\\w \\-_\\dа-яА-ЯёЁ]{1,48}[a-zA-Zа-яА-ЯёЁ]$[^\\S\\W \\\\]?",
                    ),
                ],
                verbose_name="Title",
            ),
        ),
    ]
