# Generated by Django 4.0.4 on 2022-05-31 04:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("maps", "0005_remove_maps_category"),
    ]

    operations = [
        migrations.AddField(
            model_name="maps",
            name="category",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="maps.categoryofmaps",
            ),
        ),
    ]
