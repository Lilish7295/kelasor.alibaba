# Generated by Django 4.2 on 2023-12-14 08:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buses', '0002_alter_terminal_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='bus',
            name='destination',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
