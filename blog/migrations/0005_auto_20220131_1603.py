# Generated by Django 3.2.11 on 2022-01-31 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20220131_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='destination',
            field=models.TextField(default=',0'),
        ),
        migrations.AlterField(
            model_name='post',
            name='tag',
            field=models.TextField(default=',0'),
        ),
    ]
