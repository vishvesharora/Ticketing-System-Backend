# Generated by Django 4.0.2 on 2022-08-09 07:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_ticket_description_alter_ticket_priority'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='assignedTo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, to_field='username'),
            preserve_default=False,
        ),
    ]
