# Generated by Django 3.0.5 on 2020-04-25 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='massage',
            new_name='message',
        ),
    ]
