# Generated by Django 5.1.1 on 2024-12-05 18:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0002_task_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='is_complete',
        ),
    ]
