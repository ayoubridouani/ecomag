# Generated by Django 3.0.2 on 2020-01-26 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20200126_1559'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='primaryCategory',
        ),
        migrations.AlterField(
            model_name='category',
            name='slug',
            field=models.SlugField(default='', verbose_name='Identifiant'),
        ),
    ]
