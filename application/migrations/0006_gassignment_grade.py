# Generated by Django 3.1 on 2020-09-09 07:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_auto_20200908_2105'),
    ]

    operations = [
        migrations.AddField(
            model_name='gassignment',
            name='grade',
            field=models.FloatField(default=0),
        ),
    ]
