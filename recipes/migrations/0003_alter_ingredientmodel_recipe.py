# Generated by Django 5.1.6 on 2025-02-28 13:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_rename_incridientmodel_ingredientmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ingredientmodel',
            name='recipe',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recipes.recipemodel'),
        ),
    ]
