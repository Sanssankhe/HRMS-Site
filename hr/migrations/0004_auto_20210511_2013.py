# Generated by Django 2.0.2 on 2021-05-11 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0003_leave'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leave',
            name='end',
        ),
        migrations.RemoveField(
            model_name='leave',
            name='start',
        ),
        migrations.AddField(
            model_name='leave',
            name='dateend',
            field=models.CharField(default='some string', max_length=50),
        ),
        migrations.AddField(
            model_name='leave',
            name='datestart',
            field=models.CharField(default='some string', max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='nam',
            field=models.CharField(default='name', max_length=30),
        ),
    ]