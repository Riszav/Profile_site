# Generated by Django 4.2.9 on 2024-01-26 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cars',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AlterModelTable(
            name='cars',
            table='cars',
        ),
    ]
