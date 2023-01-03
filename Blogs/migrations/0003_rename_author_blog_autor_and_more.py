# Generated by Django 4.1.3 on 2023-01-02 23:23

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogs', '0002_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='author',
            new_name='autor',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='date_blog',
            new_name='fecha_publicacion',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='image',
            new_name='imagen',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='subtitle',
            new_name='nombre_locacion',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='title',
            new_name='titulo',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='content',
        ),
        migrations.AddField(
            model_name='blog',
            name='opinion',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]