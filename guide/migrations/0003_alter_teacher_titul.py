# Generated by Django 4.0.4 on 2022-04-13 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('guide', '0002_teacher_subject_subjectinfo_teachers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='titul',
            field=models.CharField(choices=[('Mgr.', 'Mgr.'), ('Ing.', 'Ing.'), ('RNDr.', 'RNDr.')], help_text='Zadejte titul učitele', max_length=7, verbose_name="Teacher 's Title"),
        ),
    ]
