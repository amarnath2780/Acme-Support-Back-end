# Generated by Django 4.1.5 on 2023-01-14 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('superuser', '0002_alter_department_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=200, unique=True),
        ),
    ]
