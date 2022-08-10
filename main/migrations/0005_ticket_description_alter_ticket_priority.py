# Generated by Django 4.0.2 on 2022-08-09 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_ticket_priority_alter_ticket_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='description',
            field=models.CharField(default='default', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='priority',
            field=models.CharField(choices=[('low', 'LOW'), ('medium', 'MEDIUM'), ('high', 'HIGH')], default='low', max_length=30),
        ),
    ]