# Generated by Django 3.2.2 on 2021-05-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picApp', '0006_auto_20210518_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(default='category.svg', upload_to='images'),
        ),
    ]