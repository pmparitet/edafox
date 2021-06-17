from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.urls import reverse
from .models import Recipes, ArticlesRecipes, CardRecipe
from main.views import get_shops_menu


def recipes(request, recipe_name):
    # выводим страницу рецепта по name
    data_page = get_object_or_404(Recipes, name=recipe_name)

    if data_page.is_active:
        # загружает магазины для меню
        shops = get_shops_menu()

        # поиск пошагового описания (картинки и текст)
        articles_recipes = ArticlesRecipes.objects.filter(recipe=data_page.pk, is_active=True).order_by('step')
        content = {
            'data_page': data_page,
            'shops': shops,
            'articles_recipes': articles_recipes,
            'kitchen_recipes': True,
        }
    else:
        return HttpResponseRedirect(reverse('kitchen:recipes_all'))

    return render(request, 'kitchenapp/recipe.html', content)


def recipes_all(request):
    # вывод всех активных рецептов
    data_page = CardRecipe.objects.filter(is_active=True).order_by('add_datetime')

    # загружает магазины для меню
    shops = get_shops_menu()

    # пагинация
    page = request.GET.get('page')
    paginator = Paginator(data_page, 9)
    try:
        recipe_paginator = paginator.page(page)
    except PageNotAnInteger:
        recipe_paginator = paginator.page(1)
    except EmptyPage:
        recipe_paginator = paginator.page(paginator.num_pages)

    content = {
        'data_page': recipe_paginator,
        'shops': shops,
    }
    return render(request, 'kitchenapp/recipes_all.html', content)
