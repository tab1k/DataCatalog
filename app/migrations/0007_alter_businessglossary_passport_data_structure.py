# Generated by Django 5.0.4 on 2024-04-16 13:08

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0006_businessglossary"),
    ]

    operations = [
        migrations.AlterField(
            model_name="businessglossary",
            name="passport_data_structure",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="app.passport"
            ),
        ),
    ]
