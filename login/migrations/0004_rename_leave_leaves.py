# Generated by Django 4.0.3 on 2022-03-23 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0003_leave'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='leave',
            new_name='leaves',
        ),
    ]
