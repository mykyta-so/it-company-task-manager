# Generated by Django 5.0.7 on 2024-08-12 21:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0013_alter_task_deadline"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="assignees",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="tasks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="priority",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="task_manager.taskpriority",
            ),
        ),
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="task_manager.tasktype",
            ),
        ),
        migrations.AlterField(
            model_name="worker",
            name="position",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="workers",
                to="task_manager.position",
            ),
        ),
    ]
