from django.shortcuts import render
from . import models
from django.views import generic

class AllClothes(generic.ListView):
    template_name='clothes/all_clothes.html'
    context_object_name = 'all_clothes'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

    
class ChildrenClothes(generic.ListView):
    template_name = 'clothes/children.html'
    context_object_name = 'children'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='детская одежда').order_by('-id')

    
class TeenageClothes(generic.ListView):
    template_name='clothes/teenage.html'
    context_object_name = 'teenage'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='подростковая одежда').order_by('-id')
    
class AdultClothes(generic.ListView):
    template_name='clothes/adult.html'
    context_object_name = 'adult'
    model = models.Clothes

    def get_queryset(self):
        return self.model.objects.filter(tags__name='взрослая одежда').order_by('-id')
