# Generated by Django 5.0.7 on 2024-07-26 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0033_pdfupload_div_prn'),
    ]

    operations = [
        migrations.AddField(
            model_name='pdfupload',
            name='new_pdf',
            field=models.BooleanField(default=False),
        ),
    ]