# Generated by Django 5.0.6 on 2024-06-19 12:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_pdfmodel_category_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='MachineType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='category',
            name='files',
            field=models.ManyToManyField(related_name='category', to='events.pdfmodel'),
        ),
        migrations.CreateModel(
            name='MachineTypeFile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='machine_files')),
                ('machine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='files', to='events.machinetype')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
