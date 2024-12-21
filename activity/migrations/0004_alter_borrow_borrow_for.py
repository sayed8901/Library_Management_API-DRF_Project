# Generated by Django 4.2.4 on 2024-12-21 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activity', '0003_alter_borrow_borrow_for'),
    ]

    operations = [
        migrations.AlterField(
            model_name='borrow',
            name='borrow_for',
            field=models.PositiveSmallIntegerField(choices=[(1, '1 days'), (3, '3 days'), (5, '5 days'), (7, '7 days'), (10, '10 days'), (15, '15 days'), (30, '30 days')], default=3),
        ),
    ]