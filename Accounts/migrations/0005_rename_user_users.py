# Generated by Django 4.1.3 on 2023-01-02 13:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0004_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='user',
            new_name='Users',
        ),
    ]
