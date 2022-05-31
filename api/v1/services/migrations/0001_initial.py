# Generated by Django 4.0.4 on 2022-05-31 05:51

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ServiceCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='service_category/')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Service Category',
                'verbose_name_plural': 'Service Categories',
                'db_table': 'service_category',
            },
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', ckeditor.fields.RichTextField()),
                ('requirement_dockument', ckeditor.fields.RichTextField()),
                ('orgination', models.CharField(max_length=255)),
                ('responsible_person', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('legal_basis', models.CharField(max_length=255)),
                ('contact_number', models.CharField(max_length=50)),
                ('extra_phone_number', models.CharField(blank=True, max_length=50, null=True)),
                ('tg_link', models.CharField(blank=True, max_length=60, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('service_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='services.servicecategory')),
            ],
            options={
                'verbose_name': 'Service',
                'verbose_name_plural': 'Services',
                'db_table': 'service',
                'ordering': ['-created_at'],
            },
        ),
    ]