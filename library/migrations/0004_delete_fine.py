# Generated by Django 4.2.4 on 2024-12-21 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_remove_book_borrowed_by'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Fine',
        ),
    ]
