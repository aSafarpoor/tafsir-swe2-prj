# Generated by Django 2.1.7 on 2019-05-14 19:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0017_auto_20190514_1931'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='course',
        ),
    ]
