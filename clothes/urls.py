from django.urls import path
from . import views

urlpatterns = [
    path('all_clothes/', views.AllClothes.as_view(), name='all_clothes'),
    path('children/', views.ChildrenClothes.as_view(), name='children_clothes'),
    path('teenage/', views.TeenageClothes.as_view(), name='teenage_clothes'),
    path('adult/', views.AdultClothes.as_view(), name='adult_clothes'),
]
