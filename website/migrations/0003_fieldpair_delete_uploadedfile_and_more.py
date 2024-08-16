# Generated by Django 5.0.6 on 2024-06-21 17:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_pdfupload_uploadedfile'),
    ]

    operations = [
        migrations.CreateModel(
            name='FieldPair',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('field1', models.CharField(max_length=255)),
                ('field2', models.CharField(max_length=255)),
            ],
        ),
        migrations.DeleteModel(
            name='UploadedFile',
        ),
        migrations.RenameField(
            model_name='pdfupload',
            old_name='pdf',
            new_name='pdf_file',
        ),
        migrations.RemoveField(
            model_name='pdfupload',
            name='title',
        ),
        migrations.RemoveField(
            model_name='pdfupload',
            name='uploaded_at',
        ),
        migrations.AddField(
            model_name='fieldpair',
            name='pdf_upload',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='field_pairs', to='website.pdfupload'),
        ),
    ]
