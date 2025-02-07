from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from . import models

def book_list_view(request):
    if request.method == 'GET':
        query = models.BookModel.objects.all().order_by('-id')
        context_object_name = {
            'book': query,
        }
        return render(request, template_name='book.html',context=context_object_name)

def book_detail_view(request,id):
    if request.method == 'GET':
        query = get_object_or_404(models.BookModel,id=id)
        context_object_name = {
            'book_id': query,
        }
        return render(request, template_name='book_detail.html',context=context_object_name)

    

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