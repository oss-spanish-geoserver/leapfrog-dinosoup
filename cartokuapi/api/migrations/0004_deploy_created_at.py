# Generated by Django 2.1.1 on 2018-09-27 14:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_app_deploy'),
    ]

    operations = [
        migrations.AddField(
            model_name='deploy',
            name='created_at',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
