from django import forms


class RecipesFilterForms(forms.Form):
    find_recipe = forms.CharField(label="Название рецепта", required=False)



