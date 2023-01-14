# Generated by Django 4.1.5 on 2023-01-14 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickets',
            name='status',
            field=models.CharField(blank=True, choices=[('open', 'Open'), ('closed', 'Closed'), ('on_hold', 'On Hold')], default='open', max_length=200),
        ),
    ]