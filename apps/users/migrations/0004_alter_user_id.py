# Generated by Django 5.0.4 on 2024-04-29 13:31

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0003_alter_user_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("91d9b4ca-526e-4d88-9cd7-c6e4a47f46b8"),
                editable=False,
                unique=True,
            ),
        ),
    ]