# Generated by Django 4.2.7 on 2024-01-22 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_notification_event_alter_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='message',
            field=models.CharField(max_length=250),
        ),
    ]