# Generated by Django 3.2.2 on 2021-05-18 09:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picApp', '0008_auto_20210518_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tag', to='picApp.blogcat'),
        ),
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='category', to='picApp.blogcat'),
        ),
    ]
