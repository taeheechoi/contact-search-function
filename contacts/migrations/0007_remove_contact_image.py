# Generated by Django 2.0.6 on 2018-07-04 19:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20180704_1243'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='image',
        ),
    ]