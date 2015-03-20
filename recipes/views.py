from django.http.response import HttpResponse
from django.shortcuts import render_to_response
from recipes.models import Recipe, Comments
from django.contrib import auth

# Create your views here.
def recipes(request):
    return render_to_response('recipes.html', {'recipes':Recipe.objects.all()})

def recipe(request, recipe_id=1):
    return render_to_response('recipe.html', {'recipe':Recipe.objects.get(id=recipe_id), 'comments':Comments.objects.filter(comments_recipe_id=recipe_id)})