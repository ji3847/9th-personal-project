# Generated by Django 3.2.7 on 2021-09-21 20:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movielog', '0002_alter_movielog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='movielog',
            name='image',
        ),
    ]
