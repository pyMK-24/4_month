from . import models
from django import forms

class RecipeModelForm(forms.ModelForm):
    class Meta:
        model = models.RecipeModel
        fields = ['title','description']
        
class IngredientModelForm(forms.ModelForm):
    class Meta:
        model = models.IngredientModel
        fields = ['name','quantity','recipe']