# Generated by Django 4.0.2 on 2022-08-07 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='createdAt',
            field=models.DateTimeField(auto_now_add=True, verbose_name='createdAt'),
        ),
    ]