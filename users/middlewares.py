from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponseBadRequest

junior_delevoper = 'начинающего разработчика.Заработная плата:500-1000$'
middle_delevoper = 'среднего разработчика.Заработная плата:1000-2000$'
senior_delevoper = 'старшего разработчика.Заработная плата:2000-3000$'

class YearPositionMiddleware(MiddlewareMixin):
    def procces_request(self, request):
        if request.path == '/register/' and request.method == 'POST':
            year = int(request.POST.get('year'))
            if year < 1:
                return HttpResponseBadRequest('Ваш год работы не может быть меньше 1')
            elif year > 1 and year < 3:
                request.position = junior_delevoper
            elif year > 3 and year < 8:
                request.position = middle_delevoper
            elif year > 8 and year <= 15:
                request.position = senior_delevoper
            else:
                return HttpResponseBadRequest('Вы профессионал в этом деле.Вы выше все этого ;)')
        elif request.path == '/register/' and request.method == 'GET':
            setattr(request, 'position', 'Позиция не найдена.' )  
