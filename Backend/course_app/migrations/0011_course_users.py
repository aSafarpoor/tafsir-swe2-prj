# Generated by Django 2.1.7 on 2019-05-12 19:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0010_auto_20190512_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.IntegerField(default=0),
        ),
    ]
