from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/',views.basket_list, name='basket_lst'),
    path('basket_list/<int:id>/delete/',views.delete_basket_view, name='delete_basket'),
    path('basket_list/<int:id>/update/',views.update_basket_view, name='update_basket'),
    path('create_basket/',views.create_basket, name='create_basket'),
]