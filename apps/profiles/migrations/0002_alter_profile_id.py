# Generated by Django 5.0.4 on 2024-04-29 13:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("217773ff-9a10-46e0-b106-7e7a15169044"),
                editable=False,
                unique=True,
            ),
        ),
    ]
