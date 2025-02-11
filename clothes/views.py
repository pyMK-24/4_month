from django.shortcuts import render
from . import models

def all_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.all().order_by('-id')
        context_object_name = {
            'all_clothes': query,
        }
        return render(request,template_name='clothes/all_clothes.html',context=context_object_name)
    
def children_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name='детская одежда').order_by('-id')
        context_object_name = {
            'children': query,
        }
        return render(request,template_name='clothes/children.html',context=context_object_name)
    
def teenage_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name='подростковая одежда').order_by('-id')
        context_object_name = {
            'teenage': query,
        }
        return render(request,template_name='clothes/teenage.html',context=context_object_name)
    
def adult_clothes(request):
    if request.method == 'GET':
        query = models.Clothes.objects.filter(tags__name='взрослая одежда').order_by('-id')
        context_object_name = {
            'adult': query,
        }
        return render(request,template_name='clothes/adult.html',context=context_object_name)