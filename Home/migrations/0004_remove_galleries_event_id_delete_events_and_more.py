# Generated by Django 5.1.5 on 2025-03-05 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_events_galleries_delete_artists'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='galleries',
            name='event_id',
        ),
        migrations.DeleteModel(
            name='Events',
        ),
        migrations.DeleteModel(
            name='Galleries',
        ),
    ]
