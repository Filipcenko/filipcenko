# Generated by Django 5.0 on 2024-07-04 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_remove_task_customer_task_client_alter_task_employee_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, default='', max_length=15, null=True, unique=True),
        ),
    ]