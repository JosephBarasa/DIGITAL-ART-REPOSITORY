# Generated by Django 5.1.7 on 2025-04-26 10:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Artworks', '0015_alter_order_artwork'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='status',
        ),
        migrations.AddField(
            model_name='order',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
    ]
