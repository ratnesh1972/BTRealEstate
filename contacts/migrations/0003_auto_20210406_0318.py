# Generated by Django 3.1.7 on 2021-04-06 03:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20210406_0314'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]