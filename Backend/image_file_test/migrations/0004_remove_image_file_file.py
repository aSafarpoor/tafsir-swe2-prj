# Generated by Django 2.1.7 on 2019-06-04 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('image_file_test', '0003_auto_20190604_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image_file',
            name='file',
        ),
    ]
