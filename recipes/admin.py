from django.contrib import admin
from . import models

admin.register(models.RecipeModel)
admin.register(models.IngredientModel)