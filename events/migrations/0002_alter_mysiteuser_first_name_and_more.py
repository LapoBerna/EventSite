# Generated by Django 5.0.6 on 2024-06-10 11:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mysiteuser',
            name='first_name',
            field=models.CharField(max_length=120),
        ),
        migrations.AlterField(
            model_name='mysiteuser',
            name='last_name',
            field=models.CharField(max_length=120),
        ),
    ]
