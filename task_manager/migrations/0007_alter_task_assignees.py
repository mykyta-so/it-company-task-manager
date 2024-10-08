# Generated by Django 5.0.7 on 2024-07-18 17:47

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0006_alter_task_assignees"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignees",
            field=models.ManyToManyField(
                blank=True, related_name="tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
