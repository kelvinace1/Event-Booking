# Generated by Django 4.2.7 on 2024-01-22 14:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0013_notification_event_notification_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.event'),
        ),
        migrations.AlterField(
            model_name='notification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
