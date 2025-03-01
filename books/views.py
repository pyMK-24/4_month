from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from datetime import datetime
from . import models,forms
from django.views import generic

class SearchView(generic.ListView):
    template_name = 'book.html'
    
    def get_queryset(self):
        return models.BookModel.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context
    
class BookListView(generic.ListView):
    template_name = 'book.html'
    model = models.BookModel
    
    def get_queryset(self):
        return self.model.objects.all()

def book_detail_view(request,id):
    if request.method == 'GET':
        form = forms.ReviewForm()
        query = get_object_or_404(models.BookModel,id=id)
        context_object_name = {
            'book_id': query,
            'form': form,
        }
        return render(request, template_name='book_detail.html',context=context_object_name)
    
    elif request.method == "POST":
        form = forms.ReviewForm(request.POST)
        print(forms)
        if form.is_valid():
            review = form.save(commit=False)
            review.choice_book = get_object_or_404(models.BookModel, id=id)
            review.save()
            return redirect('book_detail',id=id)
        else:
            return HttpResponse('форма не валидна')

    

def about_me(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Name: Karim</h1>'
                            '<h1>Surname: Mokhammad</h1>'
                            '<h1>Age:18</h1>')
    
def text_photo(request):
    if request.method == 'GET':
        return HttpResponse('<h1>Picture:</h1>'
                            '<img src="https://wallpapers.com/images/featured/coolest-pictures-88c269e953ar0aw4.jpg"/>')

def time(request):
    if request.method == 'GET':
        time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f'<h1>Time: {time}</h1>')