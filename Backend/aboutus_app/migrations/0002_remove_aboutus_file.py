# Generated by Django 2.1.7 on 2019-07-07 11:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='aboutus',
            name='file',
        ),
    ]
