# Generated by Django 4.2.7 on 2024-01-16 21:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_alter_event_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ticket',
            name='event',
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
