from django.db import models

class RecipeModel(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название рецепта')
    description = models.TextField(verbose_name='Опитсание рецепта')

    def __str__(self):
        return self.title

class IngredientModel(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название ингридиентов')
    quantity = models.FloatField(verbose_name='Количество')
    recipe = models.ForeignKey(RecipeModel, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.name} - {self.quantity} - {self.recipe}"