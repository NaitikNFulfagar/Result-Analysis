# Generated by Django 5.0.6 on 2024-06-23 18:20

import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0021_templates_obj_created_by1_alter_pdfupload_temp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pdfupload',
            name='temp',
            field=models.CharField(choices=website.models.templates_choices, max_length=100),
        ),
    ]
