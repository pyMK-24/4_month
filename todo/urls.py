from django.urls import path
from . import views

urlpatterns = [
    path('todo_list/',views.todo_list, name='todo_lst'),
    path('todo_list/<int:id>/delete/',views.delete_todo_view, name='delete_todo'),
    path('todo_list/<int:id>/update/',views.update_todo_view, name='update_todo'),
    path('create_todo/',views.create_todo, name='create_todo'),
]
