# Generated by Django 4.2.7 on 2024-01-25 23:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0022_alter_event_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='quantity',
            field=models.IntegerField(),
        ),
    ]
