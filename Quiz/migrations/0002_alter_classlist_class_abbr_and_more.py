# Generated by Django 5.0.6 on 2024-07-16 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classlist',
            name='class_abbr',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='classlist',
            name='class_level',
            field=models.CharField(max_length=50),
        ),
    ]
