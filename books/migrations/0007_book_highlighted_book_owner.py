# Generated by Django 4.2 on 2023-05-07 10:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0006_rename_author_id_book_author_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='highlighted',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='book',
            name='owner',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
