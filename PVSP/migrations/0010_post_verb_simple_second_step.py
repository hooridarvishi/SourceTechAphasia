# Generated by Django 4.2.1 on 2024-10-08 17:14

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("PVSP", "0009_note_verb_simple_second_step"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="verb_simple_second_step",
            field=models.CharField(blank=True, max_length=320, null=True),
        ),
    ]
