# Generated by Django 4.2 on 2023-04-29 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0003_alter_author_name'),
        ('books', '0004_rename_author_name_book_author_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='author_id',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='authors.author', to_field='name'),
        ),
    ]
