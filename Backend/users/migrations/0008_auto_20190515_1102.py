# Generated by Django 2.1.7 on 2019-05-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0007_customuser_image_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='image_url',
        ),
        migrations.AddField(
            model_name='customuser',
            name='image',
            field=models.ImageField(default='', upload_to='pic_folder/'),
        ),
    ]
