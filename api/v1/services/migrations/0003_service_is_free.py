# Generated by Django 4.0.4 on 2022-05-31 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_alter_service_legal_basis'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='is_free',
            field=models.BooleanField(default=False),
        ),
    ]