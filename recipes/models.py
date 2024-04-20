from time import timezone

from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone


class Recipe(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    steps = models.TextField()
    cooking_time = models.PositiveIntegerField()  # время приготовления в минутах
    image = models.ImageField(upload_to='recipe_images/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    published_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Ingredient(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RecipeCategory(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('recipe', 'category')

    def __str__(self):
        return f"{self.recipe.title} - {self.category.name}"


