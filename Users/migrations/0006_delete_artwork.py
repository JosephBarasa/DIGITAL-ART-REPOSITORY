# Generated by Django 5.1.5 on 2025-03-05 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0005_remove_artwork_created_at_artwork_year'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Artwork',
        ),
    ]
