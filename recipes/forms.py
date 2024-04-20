from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'steps', 'cooking_time', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'steps': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
