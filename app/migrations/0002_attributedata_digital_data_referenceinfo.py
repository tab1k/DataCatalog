# Generated by Django 5.0.4 on 2024-04-04 09:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="attributedata",
            name="digital_data",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="app.digitaldata",
            ),
        ),
        migrations.CreateModel(
            name="ReferenceInfo",
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
                ("info", models.TextField()),
                (
                    "digital_data",
                    models.ForeignKey(
                        default=None,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.digitaldata",
                    ),
                ),
            ],
        ),
    ]
