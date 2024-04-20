from django.shortcuts import render, redirect
from .models import Recipe
from .forms import RecipeForm


def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes': recipes})


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_add(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipes:recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_add.html', {'form': form})


def recipe_edit(request, pk):
    recipe = Recipe.objects.get(pk=pk)
    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipes/recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipes/recipe_edit.html', {'form': form})


# def delete_recipe(request, recipe_id):
#     recipe = Recipe.objects.get(pk=recipe_id)
#     recipe.delete()
#     return redirect('recipes/recipe_list')
