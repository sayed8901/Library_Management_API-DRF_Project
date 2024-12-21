# Generated by Django 4.2.4 on 2024-12-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0006_remove_borrow_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrow',
            name='fine',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=6),
        ),
    ]
