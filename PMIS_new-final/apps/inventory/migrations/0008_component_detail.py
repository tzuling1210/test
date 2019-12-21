# Generated by Django 2.0 on 2018-12-22 07:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20181220_1548'),
    ]

    operations = [
        migrations.CreateModel(
            name='Component_detail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year_demand', models.PositiveIntegerField(blank=True, null=True)),
                ('holding_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('setup_cost', models.PositiveIntegerField(blank=True, null=True)),
                ('epq', models.DecimalField(decimal_places=2, max_digits=5)),
                ('component_name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='inventory.Component')),
            ],
        ),
    ]