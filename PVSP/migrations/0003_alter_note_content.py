# Generated by Django 4.2.1 on 2024-10-02 23:48

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PVSP", "0002_note"),
    ]

    operations = [
        migrations.AlterField(
            model_name="note",
            name="content",
            field=models.CharField(max_length=320),
        ),
    ]
