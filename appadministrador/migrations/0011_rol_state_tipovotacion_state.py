# Generated by Django 4.2.17 on 2025-01-12 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appadministrador', '0010_alter_plancha_id_tipovotacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='rol',
            name='state',
            field=models.IntegerField(default=1),
        ),
        migrations.AddField(
            model_name='tipovotacion',
            name='state',
            field=models.IntegerField(default=1),
        ),
    ]
