# Generated by Django 5.0.4 on 2024-05-12 19:48

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0005_alter_profile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("66418a6f-90a8-4ce0-a98c-01d30b338a14"),
                editable=False,
                unique=True,
            ),
        ),
    ]