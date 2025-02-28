from django.shortcuts import render, redirect, get_object_or_404
from . import models, forms
from django.views import generic
from django.urls import reverse_lazy

class RecipeView(generic.ListView):
    template_name = 'recipes/recipe_list.html'
    context_object_name = 'recipe_list'
    model = models.RecipeModel
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-id')

class RecipeDetailView(generic.DetailView):
    template_name = "recipes/recipe_detail.html"
    context_object_name = "recipe"
    model = models.RecipeModel
    
class CreateRecipeView(generic.CreateView):
    template_name = 'recipes/create_recipe.html'
    form_class = forms.RecipeModelForm
    success_url = reverse_lazy('recipe_list')

class CreateIngredientsView(generic.CreateView):
    template_name = 'recipes/create_ingredient.html'
    model = models.IngredientModel
    form_class = forms.IngredientModelForm
    
    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.recipe.id})

class DeleteRecipeView(generic.DeleteView):
    template_name = 'recipes/recipe_confirm_del.html'
    model = models.RecipeModel
    success_url = reverse_lazy('recipe_list')

class DeleteIngredientView(generic.DeleteView):
    template_name = 'recipes/ingredient_confirm_del.html'
    model = models.IngredientModel

    def get_success_url(self):
        return reverse_lazy("recipe_detail", kwargs={"pk": self.object.recipe.id})
