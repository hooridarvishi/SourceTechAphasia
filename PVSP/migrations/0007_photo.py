# Generated by Django 4.2.1 on 2024-10-03 01:04

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PVSP", "0006_post"),
    ]

    operations = [
        migrations.CreateModel(
            name="Photo",
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
                ("image", models.ImageField(upload_to="photos/")),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]
