# Generated by Django 2.1.7 on 2019-04-01 22:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listing',
            old_name='state',
            new_name='county',
        ),
    ]
