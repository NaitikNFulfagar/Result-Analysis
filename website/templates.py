from django.shortcuts import render,redirect
from django.contrib import messages
from .forms import AddtemplatesForm
from .models import templates_obj
import json
from django.db.models import Case, When, IntegerField


def templates_record(request,pk):
    if request.user.is_authenticated:
        customer_record = templates_obj.objects.get(id=pk)
        return render(request,'templ/templates_record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You Must Be Logged In To View This Page.....")
        return redirect('login')
    
def delete_templates(request,pk):
    if request.user.is_authenticated:
        delete_it = templates_obj.objects.get(id=pk)
        delete_it.delete()
        messages.success(request,"Records Deleted Successfully...!")
        return redirect('templates')
    else:
        messages.success(request,"You Must Be Logged In To View This Page.....")
        return redirect('login')

import logging

logger = logging.getLogger(__name__)

def add_templates(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddtemplatesForm(request.POST or None)
            if form.is_valid():
                upload = form.save(commit=False)
                try:
                    key_value_pairs_json = request.POST.get('key_value_pairs', '[]')
                    key_value_pairs = json.loads(key_value_pairs_json)
                    upload.key_value_pairs = key_value_pairs
                    upload.created_by = request.user.get_full_name()
                    logger.error(request.user.get_full_name())
                    upload.save()
                    messages.success(request, "Records Added Successfully...!")
                    return redirect('templates')
                except json.JSONDecodeError as e:
                    logger.error(f"JSON decode error: {str(e)}")
                    form.add_error(None, 'Invalid JSON format')
            else:
                logger.error(f"Form is not valid: {form.errors}")
                form.add_error(None, 'Form is not valid')
        else:
            form = AddtemplatesForm()
        return render(request, 'templ/add_templates.html', {'form': form})
    else:
        messages.success(request, "You Must Be Logged In To View This Page.....")
        return redirect('login')

def update_templates(request, pk):
    record = templates_obj.objects.get(id=pk)
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = AddtemplatesForm(request.POST, instance=record)
            if form.is_valid():
                upload = form.save(commit=False)
                try:
                    key_value_pairs_json = request.POST.get('key_value_pairs', '[]')
                    key_value_pairs = json.loads(key_value_pairs_json)
                    upload.key_value_pairs = key_value_pairs
                    #upload.created_by = request.user.get_full_name()
                    logger.error(key_value_pairs)
                    upload.save()
                    messages.success(request, "Records Updated Successfully...!")
                    return redirect('templates')
                except json.JSONDecodeError as e:
                    logger.error(f"JSON decode error: {str(e)}")
                    form.add_error(None, 'Invalid JSON format')
            else:
                logger.error(f"Form is not valid: {form.errors}")
                form.add_error(None, 'Form is not valid')
        else:
            form = AddtemplatesForm(instance=record)
        return render(request, 'templ/update_templates.html', {'form': form, 'key_value_pairs': record.key_value_pairs, 'update': True, 'record': record})
    else:
        messages.success(request, "You Must Be Logged In To View This Page.....")
        return redirect('login')

# def update_templates(request,pk):
#     if request.user.is_authenticated:
#         current_record = templates_obj.objects.get(id=pk)
#         form = AddtemplatesForm(request.POST or None,instance=current_record)
#         if form.is_valid():
#             form.save()
#             messages.success(request,"Records Updated Successfully...!")
#             return redirect('templates')
#         return render(request,'templ/update_templates.html',{'form':form})
#     else:
#         messages.success(request,"You Must Be Logged In To View This Page.....")
#         return redirect('login')
    
    
def templates(request):
    
    if request.user.is_authenticated:
        records = templates_obj.objects.all().order_by(
    Case(
        When(Name__startswith='FE', then=1),
        When(Name__startswith='SE', then=2),
        When(Name__startswith='TE', then=3),
        When(Name__startswith='BE', then=4),
        default=999,
        output_field=IntegerField(),
    )
)
        return render(request,'templates.html',{'records':records})

    else:
        messages.success(request,"You Must Be Logged In To View This Page.....")
        return redirect('login')
    
