# Generated by Django 4.1.7 on 2024-01-21 10:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_remove_contactprofile_is_active'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contactprofile',
            old_name='message',
            new_name='messages',
        ),
    ]