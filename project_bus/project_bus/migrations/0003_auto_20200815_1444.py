# Generated by Django 2.2.10 on 2020-08-15 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_bus', '0002_auto_20200815_1442'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='routes',
            field=models.ManyToManyField(related_name='stations', to='project_bus.Route'),
        ),
    ]
