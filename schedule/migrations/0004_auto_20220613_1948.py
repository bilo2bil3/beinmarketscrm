# Generated by Django 3.1.4 on 2022-06-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedule', '0003_auto_20220613_1941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='schedule',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='schedule',
            name='time',
            field=models.TimeField(),
        ),
    ]