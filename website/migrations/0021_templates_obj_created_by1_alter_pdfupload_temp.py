# Generated by Django 5.0.6 on 2024-06-23 18:19

import datetime
import website.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0020_alter_pdfupload_created_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='templates_obj',
            name='created_by1',
            field=models.CharField(choices=website.models.year_choices_fun, default=datetime.datetime(2024, 6, 23, 18, 19, 54, 68267, tzinfo=datetime.timezone.utc), max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pdfupload',
            name='temp',
            field=models.CharField(max_length=100),
        ),
    ]
