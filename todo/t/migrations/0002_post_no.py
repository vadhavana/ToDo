# Generated by Django 2.0.8 on 2018-08-24 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('t', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='no',
            field=models.IntegerField(default=None),
        ),
    ]