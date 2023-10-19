# Generated by Django 4.2.6 on 2023-10-11 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopsy", "0002_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="Registration",
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
                ("first_name", models.CharField(blank=True, max_length=50, null=True)),
                ("last_name", models.CharField(blank=True, max_length=50, null=True)),
                ("phone", models.CharField(blank=True, max_length=10, null=True)),
                ("email", models.EmailField(max_length=254)),
                ("password", models.CharField(blank=True, max_length=100, null=True)),
                ("gender", models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]