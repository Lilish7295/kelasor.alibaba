# Generated by Django 4.2 on 2023-12-13 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terminal',
            name='phone_number',
            field=models.CharField(max_length=11),
        ),
    ]
