# Generated by Django 2.2.3 on 2019-07-27 02:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_notification'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notification',
            old_name='destination',
            new_name='target',
        ),
    ]
