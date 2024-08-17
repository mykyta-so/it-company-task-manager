# Generated by Django 5.0.7 on 2024-07-18 14:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0004_task_priority"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignees",
            field=models.ManyToManyField(
                null=True, related_name="tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.CharField(
                choices=[
                    ("Critical", "Critical"),
                    ("High", "High"),
                    ("Medium", "Medium"),
                    ("Low", "Low"),
                    ("Optional", "Optional"),
                ],
                max_length=255,
            ),
        ),
    ]
