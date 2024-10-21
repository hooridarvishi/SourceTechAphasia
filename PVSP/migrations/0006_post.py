# Generated by Django 4.2.1 on 2024-10-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PVSP", "0005_delete_post_delete_verb"),
    ]

    operations = [
        migrations.CreateModel(
            name="Post",
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
                ("content_verb", models.TextField()),
                ("is_deleted", models.BooleanField(default=False)),
            ],
        ),
    ]