# Generated by Django 2.2 on 2019-05-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190508_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='student',
            field=models.BooleanField(default=True),
        ),
    ]