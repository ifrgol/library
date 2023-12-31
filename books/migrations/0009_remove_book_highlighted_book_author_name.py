# Generated by Django 4.2 on 2023-05-10 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0004_author_highlighted_author_owner'),
        ('books', '0008_remove_book_author_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='highlighted',
        ),
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authors.author', to_field='name'),
        ),
    ]
