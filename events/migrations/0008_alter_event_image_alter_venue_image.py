# Generated by Django 5.0.6 on 2024-06-14 10:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0007_event_image_venue_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/events'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/venues'),
        ),
    ]
