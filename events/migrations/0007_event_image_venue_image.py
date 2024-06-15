# Generated by Django 5.0.6 on 2024-06-13 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_venue_owner_alter_venue_email_alter_venue_web'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.AddField(
            model_name='venue',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
