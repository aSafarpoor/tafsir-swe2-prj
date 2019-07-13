# Generated by Django 2.1.7 on 2019-06-04 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='image_file',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='no_Name', max_length=50)),
                ('file', models.FileField(blank=True, null=True, upload_to='folanja/temp_file_dir/')),
                ('picture', models.ImageField(blank=True, default='folanja/images.png', null=True, upload_to='folanja/temp_image_dir/')),
            ],
        ),
    ]
