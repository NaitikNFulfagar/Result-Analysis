from django.urls import path,include,re_path
from . import views
from . import templates
from . import uploadpdf

urlpatterns = [
    path('', views.home,name='home'),
    path('login/', views.login_user,name='login'),
    path('dashboard/', views.dashboard,name='dashboard'),
    path('logout/', views.logout_user,name='logout'),
    
    re_path(r'^media/(?P<path>.*)$', views.protected_media,name='media'),
    
    
    #path('register/', views.register_user,name='register'),
    path('templates/templates_record/<int:pk>', templates.templates_record,name='templates_record'),
    path('templates/delete_record/<int:pk>', templates.delete_templates,name='delete_templates'),
    path('templates/add_templates/', templates.add_templates,name='add_templates'),
    path('templates/update_templates/<int:pk>', templates.update_templates,name='update_templates'),
    path('templates/', templates.templates,name='templates'),
    
    path('uploadpdf/uploadpdf_record/<int:pk>', uploadpdf.uploadpdf_record,name='uploadpdf_record'),
    path('uploadpdf/delete_uploadpdf/<int:pk>', uploadpdf.delete_uploadpdf,name='delete_uploadpdf'),
    path('uploadpdf/add_uploadpdf/', uploadpdf.add_uploadpdf,name='add_uploadpdf'),
    path('uploadpdf/update_uploadpdf/<int:pk>', uploadpdf.update_uploadpdf,name='update_uploadpdf'),
    path('uploadpdf/downloadcsv', uploadpdf.downloadcsv,name='downloadcsv'),
    #path('uploadpdf/dwdresays', uploadpdf.dwdresays,name='dwdresays'),
    path('uploadpdf/dwdresaysdocx', uploadpdf.dwdresaysdocx,name='dwdresaysdocx'),
    path('uploadpdf/', uploadpdf.uploadpdf,name='uploadpdf'),
    
]
