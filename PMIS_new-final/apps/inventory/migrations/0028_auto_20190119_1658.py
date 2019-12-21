# Generated by Django 2.0 on 2019-01-19 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0027_auto_20190119_1656'),
    ]

    operations = [
        migrations.AddField(
            model_name='component',
            name='safety_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='material',
            name='safety_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='safety_stock',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]