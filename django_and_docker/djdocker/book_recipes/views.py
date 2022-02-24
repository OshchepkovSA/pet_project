from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Q

from book_recipes.models import Recipes, Ingredients
from book_recipes.forms import RecipesFilterForms


def home(request):
    """Главная страница. Редирект на `/recipes_list`"""
    response = redirect(reverse("recipes_list"))
    return response


def recipes_list(request):
    try:
        find_recipe = request.GET.get("find_recipe")
    except (ValueError, TypeError):
        find_recipe = None
    query = Q()
    if find_recipe:
        query.add(
            Q(pk=find_recipe), Q.AND,
        )
    recs = Recipes.objects.filter(query)
    ingrs = Ingredients.objects.all()
    filter_recipes = RecipesFilterForms()
    filter_ingredients = Ingredients.objects.values('ingredient').distinct()
    return render(request, 'book_recipes/recipes_list.html', {"recs": recs,
                                                              "ingrs": ingrs,
                                                              "filter_recipes": filter_recipes,
                                                              'filter_ingredients': filter_ingredients,
                                                              })


def search_ingredients(request):
    recs = Recipes.objects.all()
    ingrs = Ingredients.objects.all()
    recipes_list = []
    check_ingrs = request.GET.getlist('check_ingrs')
    for check_ingr in check_ingrs:
        for ingr in ingrs:
            if ingr.ingredient==check_ingr:
                recipes_list.append(ingr.recipes_id)
    recipes_list = list(set(recipes_list))
    return render(request, 'book_recipes/search_ingredients.html', {'check_ingrs': check_ingrs,
                                                                    "ingrs": ingrs,
                                                                    "recs": recs,
                                                                    "recipes_list": recipes_list,
                                                                    })
