# Generated by Django 4.2 on 2023-04-27 17:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0006_alter_task_assigned_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='assigned_date',
        ),
    ]