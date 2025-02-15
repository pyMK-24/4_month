from django.shortcuts import render,redirect,get_object_or_404
from . import models,forms

def basket_list(request):
    if request.method == 'GET':
        query = models.BasketModel.objects.all()
        context_object_name = {
            'basket_lst': query
        }
        return render(request,template_name='basket/basket_list.html',context=context_object_name)

def create_basket(request):
    if request.method == 'POST':
        form = forms.BasketForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('basket_lst')
    else:
        form = forms.BasketForm()
    return render(request, template_name='basket/create_basket.html',context={'form': form})

def delete_basket_view(requst,id):
    basket_id = get_object_or_404(models.BasketModel, id=id)
    basket_id.delete()
    return redirect('basket_lst')

def update_basket_view(request,id):
    basket_id = get_object_or_404(models.BasketModel,id=id)
    if request.method == 'POST':
        form =  forms.BasketForm(request.POST,instance=basket_id)
        if form.is_valid():
            form.save()
    else:
        form = forms.BasketForm(instance=basket_id)
    return render(request,template_name='basket/update_basket.html',context={'form':form,
                                                                             'basket_id': basket_id,
                                                                             })
        
        
        
        
        
        
        
        
        
        
        

