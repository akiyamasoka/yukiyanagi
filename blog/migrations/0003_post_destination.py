# Generated by Django 3.2.11 on 2022-01-31 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='destination',
            field=models.SmallIntegerField(default=-1),
        ),
    ]
