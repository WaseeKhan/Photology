# Generated by Django 3.2.2 on 2021-05-18 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('picApp', '0011_auto_20210518_1509'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='img',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='blogcat',
            name='description',
        ),
        migrations.AddField(
            model_name='blog',
            name='blogImg',
            field=models.ImageField(default='image.svg', upload_to='blogImages'),
        ),
        migrations.AddField(
            model_name='blogcat',
            name='desc',
            field=models.TextField(max_length=200, null=True),
        ),
        migrations.DeleteModel(
            name='BlogTag',
        ),
    ]
