# Generated by Django 2.1.7 on 2019-07-12 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aboutus_app', '0006_contactus_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='time',
            field=models.TextField(blank=True, null=True),
        ),
    ]
