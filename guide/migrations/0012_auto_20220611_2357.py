# Generated by Django 3.2.9 on 2022-06-11 21:57

from django.db import migrations, models
import guide.models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0011_auto_20220605_1548'),
    ]

    operations = [
        migrations.AddField(
            model_name='code',
            name='code',
            field=models.FileField(null=True, upload_to=guide.models.code_path, verbose_name='Zdrojový kód'),
        ),
        migrations.AlterField(
            model_name='lang',
            name='desc',
            field=models.TextField(help_text='Popište programovací jazyk', verbose_name='Popis jazyka'),
        ),
    ]
