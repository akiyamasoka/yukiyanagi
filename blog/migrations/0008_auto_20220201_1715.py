# Generated by Django 3.2.11 on 2022-02-01 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20220201_1638'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='選択肢名')),
            ],
        ),
        migrations.RemoveField(
            model_name='servey',
            name='needs',
        ),
        migrations.AlterField(
            model_name='servey',
            name='question',
            field=models.TextField(verbose_name='2つ目の理由、またはサイトデザインや質問内容等に関する要望があれば教えてください。'),
        ),
        migrations.AlterField(
            model_name='servey',
            name='student_number',
            field=models.IntegerField(verbose_name='学籍番号'),
        ),
        migrations.AddField(
            model_name='servey',
            name='needs',
            field=models.ManyToManyField(to='blog.Tag', verbose_name='あなたのニーズに合った学内機関が表示されたと思いますか？'),
        ),
    ]
