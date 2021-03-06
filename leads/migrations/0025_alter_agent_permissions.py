# Generated by Django 4.0.5 on 2022-06-08 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('permissions', '0004_alter_permission_code'),
        ('leads', '0024_delete_permission_alter_agent_permissions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='permissions',
            field=models.ManyToManyField(blank=True, related_name='agent_permissions', to='permissions.permission'),
        ),
    ]
