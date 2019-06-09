# Generated by Django 2.1.7 on 2019-06-04 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='no_Name', max_length=50)),
                ('explanation', models.TextField(default='no_Name', max_length=500)),
                ('file', models.FileField(blank=True, default='folanja/images.png', null=True, upload_to='folanja/aboutus')),
            ],
        ),
    ]