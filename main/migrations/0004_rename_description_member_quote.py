# Generated by Django 5.0.1 on 2024-01-16 21:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_member_description_member_location'),
    ]

    operations = [
        migrations.RenameField(
            model_name='member',
            old_name='description',
            new_name='quote',
        ),
    ]
