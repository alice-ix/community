# Generated by Django 3.0.2 on 2020-02-02 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tag', '0001_initial'),
        ('board', '0002_auto_20200202_0008'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='tags',
            field=models.ManyToManyField(to='tag.Tag', verbose_name='태그'),
        ),
    ]
