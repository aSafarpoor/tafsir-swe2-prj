# Generated by Django 2.1.7 on 2019-07-12 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus_app', '0008_auto_20190712_1015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.TextField(blank=True, max_length=20, null=True),
        ),
    ]
