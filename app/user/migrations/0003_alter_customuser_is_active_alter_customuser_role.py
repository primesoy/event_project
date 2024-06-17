# Generated by Django 5.0.6 on 2024-06-17 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('User', 'User'), ('Moderator', 'Moderator'), ('Premium', 'Premium'), ('Admin', 'Admin')], default='User', help_text='Das ist ein Hilfetext', max_length=20),
        ),
    ]
