from django.urls import path
from . import views

urlpatterns = [
    path('mashina_list/',views.MashinaListView.as_view(), name='mashina_list'),
    path('mashina_parsing/',views.MashinaFormView.as_view(), name='parser'),
    path('rezka_list/',views.RezkaListView.as_view(), name='rezka_list'),
]