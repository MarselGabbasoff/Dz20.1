from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("catalog", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="ContactInfo",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "phone",
                    models.CharField(max_length=20, verbose_name="Номер телефона"),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="Почта")),
                ("address", models.TextField(verbose_name="Адрес")),
            ],
            options={
                "verbose_name": "Контактная информация",
                "verbose_name_plural": "Контактные информации",
            },
        ),
    ]