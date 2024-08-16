from django.contrib import admin
from .models import PDFUpload
from .models import templates_obj

admin.site.register(PDFUpload)
admin.site.register(templates_obj)

# Register your models here.
