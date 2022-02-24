from django.contrib import admin
from .models import Ingredients, Recipes


@admin.register(Recipes)
class RecipesAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "description",
    )
    search_fields = (
        "name",
        "description",
    )
    ordering = ("name", )


@admin.register(Ingredients)
class IngredientsAdmin(admin.ModelAdmin):
    list_display = (
        "recipes",
        "ingredient",
    )
    search_fields = (
        "recipes",
        "ingredient",
    )
    ordering = ("recipes", )