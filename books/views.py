from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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