# Generated by Django 4.2 on 2023-04-29 18:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_remove_book_author_book_author_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author_name',
        ),
    ]
