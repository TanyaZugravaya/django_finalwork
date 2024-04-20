from django.urls import path
from . import views

app_name = 'recipes'

urlpatterns = [
    path('', views.index, name='index'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('add/', views.recipe_add, name='recipe_add'),
    path('edit/<int:pk>/', views.recipe_edit, name='recipe_edit'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
]
