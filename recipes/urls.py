from . import views
from django.urls import path

urlpatterns = [
    path('recipe_list/', views.RecipeView.as_view(), name='recipe_list'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe_detail'),
    path('recipe/create/', views.CreateRecipeView.as_view(), name='create_recipe'),
    path('ingredient/create/<int:recipe_pk>/', views.CreateIngredientsView.as_view(), name='create_ingredient'),
    path('recipe/<int:pk>/delete/', views.DeleteRecipeView.as_view(), name='delete_recipe'),
    path('ingredient/create/<int:recipe_pk>/', views.CreateIngredientsView.as_view(), name='create_ingredient'),
]

