# Generated by Django 2.1.7 on 2019-05-15 15:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0021_auto_20190515_1350'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question_exam',
            old_name='whitch_section',
            new_name='which_section',
        ),
    ]
