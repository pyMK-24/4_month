from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms
from django.views import generic

class BasketListView(generic.ListView):
    template_name='basket/basket_list.html'
    context_object_name = 'basket_lst'
    model = models.BasketModel
    
    def  get_queryset(self):
        return self.model.objects.all().order_by('-id')
    
    

class CreateBasketView(generic.CreateView):
    template_name='basket/create_basket.html'
    form_class = forms.BasketForm
    success_url = '/basket_list/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBasketView, self).form_valid(form=form)
    
class DeleteBasketView(generic.DeleteView):
    template_name = 'basket/confirm_delete.html'
    success_url = '/basket_list/'
    
    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)
    
class UpdateBasketView(generic.UpdateView):
    template_name='basket/update_basket.html'
    form_class = forms.BasketForm
    success_url = '/basket_list/'
    
    def get_object(self, *args, **kwargs):
        basket_id = self.kwargs.get('id')
        return get_object_or_404(models.BasketModel, id=basket_id)
    
    def form_valid(self, form):
        print(form.cleaned_data)
        return super(UpdateBasketView, self).form_valid(form=form)
                
        
        
        
        
        
        
        
        
        
        

