# Generated by Django 3.1.7 on 2021-03-25 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('prediction', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentdetails',
            name='parents_satisfaction',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')]),
        ),
    ]
