from django.db import models


class Recipes(models.Model):
    name = models.TextField("Название рецепта", primary_key=True, max_length=50, unique=True, default=None)
    description = models.TextField("Описание", null=True, default=None, blank=True)

    class Meta:
        verbose_name = "Рецепт"
        verbose_name_plural = "Рецепты"

    def __str__(self):
        return self.name


class Ingredients(models.Model):
    ingredient = models.CharField("Ингредиенты", max_length=50, default=None)
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE, default=None, verbose_name="Название рецепта",
                                # related_name='recipes_id',

                                )

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"
        unique_together = [['recipes', 'ingredient']]

    def __str__(self):
        return self.ingredient
