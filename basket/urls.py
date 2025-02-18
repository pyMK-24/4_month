from django.urls import path
from . import views

urlpatterns = [
    path('basket_list/',views.BasketListView.as_view(), name='basket_lst'),
    path('basket_list/<int:id>/delete/',views.DeleteBasketView.as_view(), name='delete_basket'),
    path('basket_list/<int:id>/update/',views.UpdateBasketView.as_view(), name='update_basket'),
    path('create_basket/',views.CreateBasketView.as_view(), name='create_basket'),
]