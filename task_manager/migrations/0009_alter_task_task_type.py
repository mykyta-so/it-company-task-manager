# Generated by Django 5.0.7 on 2024-07-19 19:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("task_manager", "0008_alter_worker_position"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="task_type",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="task_manager.tasktype",
            ),
            preserve_default=False,
        ),
    ]
