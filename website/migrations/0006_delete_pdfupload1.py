# Generated by Django 5.0.6 on 2024-06-21 17:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_rename_pdfupload_pdfupload1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='PDFUpload1',
        ),
    ]
