# Generated by Django 5.1.7 on 2025-03-30 07:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0010_order_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='artwork',
        ),
    ]
