# Generated by Django 2.2.3 on 2019-07-27 02:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20190727_0952'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
