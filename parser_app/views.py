from django.shortcuts import render,HttpResponse,redirect
from django.views import generic
from . import models,forms

class MashinaListView(generic.ListView):
    template_name = 'parser_app/mashina_list.html'
    context_object_name = 'mashina'
    model = models.MashinaModel
    
    def get_queryset(self):
        return self.model.objects.all().order_by('id')

class RezkaListView(generic.ListView):
    template_name = 'parser_app/rezka_list.html'
    context_object_name = 'rezka'
    model = models.RezkaModel
    
    def get_queryset(self):
        return self.model.objects.all().order_by('id')

  
class MashinaFormView(generic.FormView):
    template_name = 'parser_app/mashina_form.html'
    form_class = forms.ParserForm
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.parser_data()
            return redirect('mashina_list')
        else:
            return super(MashinaFormView, self).post(request, *args, **kwargs)
            
