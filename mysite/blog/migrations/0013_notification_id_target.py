# Generated by Django 2.2.3 on 2019-07-27 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_notification_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='id_target',
            field=models.IntegerField(default=0),
        ),
    ]
