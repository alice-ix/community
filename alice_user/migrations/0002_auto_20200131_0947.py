# Generated by Django 3.0.2 on 2020-01-31 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alice_user', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aliceuser',
            options={'verbose_name': '앨리스 사용자', 'verbose_name_plural': '앨리스 사용자'},
        ),
        migrations.AddField(
            model_name='aliceuser',
            name='userEmail',
            field=models.EmailField(default='test@gmail.com', max_length=128, verbose_name='사용자이메일'),
            preserve_default=False,
        ),
    ]
