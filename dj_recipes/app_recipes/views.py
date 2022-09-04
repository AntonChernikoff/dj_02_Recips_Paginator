from django.shortcuts import render, reverse
from django.http import HttpResponse
# from django.urls import reverse
# from django.contrib.sites.models import Site

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
     },
    'pasta': {
         'макароны, кг': 0.3,
         'сыр, кг': 0.05,
     },
    'buter': {
         'хлеб, ломтик': 1,
         'колбаса, ломтик': 1,
         'сыр, ломтик': 1,
         'помидор, ломтик': 1,
     },
    'hot-dog': {
        'сосиска, шт': 1,
         'булочка, шт': 1,
         'кетчуп, гр': 2,
         'горчица, гр': 1,
     },
    # можете добавить свои рецепты ;)
}
def home(request):
    # return HttpResponse('Hello')
    # domain = 'http://127.0.0.1:8000/'
    # domain = reverse('home')
    recipes = {}
    for recipe in DATA.keys():
        recipes[recipe] = f"{reverse('home')}{recipe}/?servings=1"
    context = {
        'recipes': recipes
    }
    return render(request, 'app_recipes/home.html', context)

def recipe(request, dish):
    context = {
        'recipe': {},
        'home_url': reverse('home')
    }
    amount = int(request.GET.get("servings", 1))
    if dish in DATA:
        for key, value in DATA[dish].items():
            DATA[dish][key] = value * amount
        context['recipe'] = DATA[dish]
    return render(request, 'app_recipes/recipe.html', context)
