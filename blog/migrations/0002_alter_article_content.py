# Generated by Django 5.1.1 on 2024-09-17 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="content",
            field=models.TextField(verbose_name="cодержимое статьи"),
        ),
    ]