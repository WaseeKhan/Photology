# Generated by Django 3.2 on 2021-05-19 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picApp', '0015_auto_20210518_2134'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='tags',
        ),
    ]
