# Generated by Django 5.0.4 on 2024-04-29 19:36

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("profiles", "0003_alter_profile_created_at_alter_profile_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="id",
            field=models.UUIDField(
                default=uuid.UUID("03005452-b368-41e4-8734-c787545d9362"),
                editable=False,
                unique=True,
            ),
        ),
    ]