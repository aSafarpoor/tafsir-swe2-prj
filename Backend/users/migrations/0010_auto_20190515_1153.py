# Generated by Django 2.1.7 on 2019-05-15 11:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_customuser_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='image_url',
        ),
        migrations.RemoveField(
            model_name='customuser',
            name='picture2',
        ),
    ]
