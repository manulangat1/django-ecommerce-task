# Generated by Django 5.0.4 on 2024-05-13 15:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0006_alter_profile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
