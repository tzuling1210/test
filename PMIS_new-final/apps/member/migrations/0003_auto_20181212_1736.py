# Generated by Django 2.0 on 2018-12-12 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0002_auto_20181212_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='working_address',
        ),
        migrations.AddField(
            model_name='member',
            name='working_school_address',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
