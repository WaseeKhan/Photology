# Generated by Django 3.2.2 on 2021-05-18 10:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picApp', '0013_auto_20210518_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='tag',
            field=models.ManyToManyField(blank=True, related_name='tags', to='picApp.BlogTag'),
        ),
    ]
