# Generated by Django 4.0.4 on 2022-05-31 03:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("news", "0003_alter_news_options_alter_news_table"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="news",
            name="updated_at",
        ),
    ]
