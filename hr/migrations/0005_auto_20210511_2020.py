# Generated by Django 2.0.2 on 2021-05-11 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_auto_20210511_2013'),
    ]

    operations = [
        migrations.AddField(
            model_name='leave',
            name='email',
            field=models.EmailField(default='name', max_length=254),
        ),
        migrations.AddField(
            model_name='leave',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
    ]
