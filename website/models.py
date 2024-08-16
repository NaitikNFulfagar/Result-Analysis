from django.db import models
from django.contrib.auth.models import User

import datetime

def year_choices_fun():
    return [(r,r) for r in range(2019, datetime.date.today().year+1)]

def current_year():
    return datetime.date.today().year

def templates_choices():
        choices = []
        for item in templates_obj.objects.all():
              concatenated_value = f"{item.Year}_{item.Branch}"
              choices.append((concatenated_value, concatenated_value))
        return choices


class templates_obj(models.Model):
    created_at  =   models.DateTimeField(auto_now_add=True)
    created_by  =    models.CharField(max_length=100,null=True)
    key_value_pairs =   models.JSONField()
    Name            =   models.CharField(max_length=100, blank=True)  # Adjust max_length as per your naming convention
    Year_choices = (
        ('FE', 'FE'),
        ('SE', 'SE'),
        ('TE', 'TE'),
        ('BE', 'BE'),
    )
    Year            =   models.CharField(max_length=50,choices=Year_choices,default="", blank=True, null=True)
    Branch_choices = (
        ('ALL'   , 'ALL'),
        ('COMPUTER'   , 'COMPUTER'),
        ('ENTC' , 'ENTC'),
        ('ELECTRICAL'  , 'ELECTRICAL'),
        ('MECHANICAL' , 'MECHANICAL'),
        ('CIVIL' , 'CIVIL'),
    )

    Branch          =   models.CharField(max_length=50,choices=Branch_choices,default="", blank=True, null=True)

    def save(self, *args, **kwargs):
        self.Name = f"{self.Year}_{self.Branch}"
        super().save(*args, **kwargs)



    def __str__(self):
        return(f"{self.Name}")

    class Meta:
        unique_together = ('Year', 'Branch')







class PDFUpload(models.Model):


    created_by  =    models.CharField(max_length=100,null=True)
    created_at  =    models.DateTimeField(auto_now_add=True,null=False)
    pdf_file    =    models.FileField(upload_to='pdfs/',null=False)
    temp        =    models.CharField(max_length=100,choices=templates_choices)
    year        =    models.IntegerField(('year'), choices=year_choices_fun, default=current_year,null=False)
    sem_ch      =    {
        "JUNE": "JUNE",
        "DECEMBER": "DECEMBER"
    }
    sem         =   models.CharField(max_length=50,choices=sem_ch,default="", blank=True, null=True)
    status      =   models.CharField(max_length=100)
    Name        =   models.CharField(max_length=100, blank=True)  # Adjust max_length as per your naming convention
    div_PRN     =   models.JSONField(null=True)
    new_pdf     =   models.BooleanField(default=False)



    def __str__(self):
        return self.pdf_file.name
    
    def save(self, *args, **kwargs):
        if self.new_pdf==True:
            self.Name = f"NEW_{self.temp}_{self.year}_{self.sem}"
        else:
            self.Name = f"{self.temp}_{self.year}_{self.sem}"
        super().save(*args, **kwargs)







