# Generated by Django 3.2.25 on 2024-05-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='body',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='message',
            name='message',
            field=models.TextField(max_length=1000),
        ),
    ]
