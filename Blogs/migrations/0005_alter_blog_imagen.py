# Generated by Django 4.1.3 on 2023-01-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0004_nuevo_sitio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='imagen',
            field=models.ImageField(upload_to='media'),
        ),
    ]