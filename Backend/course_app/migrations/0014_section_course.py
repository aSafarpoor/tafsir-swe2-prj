# Generated by Django 2.1.7 on 2019-05-13 17:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('course_app', '0013_section'),
    ]

    operations = [
        migrations.AddField(
            model_name='section',
            name='course',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='fkcourse', to='course_app.course'),
        ),
    ]