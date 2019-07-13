# Generated by Django 2.2 on 2019-07-13 10:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VideoSend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('videofile', models.FileField(null=True, upload_to='videos/', verbose_name='')),
            ],
        ),
    ]
