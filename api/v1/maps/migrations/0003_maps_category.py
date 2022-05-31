# Generated by Django 4.0.4 on 2022-05-31 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maps', '0002_maps_subway_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='maps',
            name='category',
            field=models.CharField(choices=[('1', 'Профессиональные карты'), ('2', 'Карты для прогулок'), ('3', 'Карты для прогулок')], default='1', max_length=1),
        ),
    ]