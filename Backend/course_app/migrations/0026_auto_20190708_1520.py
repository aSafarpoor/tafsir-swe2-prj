# Generated by Django 2.1.7 on 2019-07-08 15:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0025_auto_20190708_1310'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie_link',
            old_name='link',
            new_name='msg',
        ),
    ]
