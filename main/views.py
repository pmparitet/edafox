from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from .models import Shops, Catalog, PictureCatalog
from kitchenapp.models import CardRecipe
from django.urls import reverse


def get_shops_menu():
    # загружает магазины для меню
    shops = Shops.objects.filter(category_page='shop', is_active=True)
    return shops


def index(request):
    # загружает магазины для меню и сетей
    shops = get_shops_menu()

    # загружает главную страницу
    data_page = Shops.objects.get(category_page='main', is_active=True)

    # загружает ВСЕ активные каталоги из БД
    catalog_active = Catalog.objects.filter(is_active=True).order_by('add_datetime')

    # вывод всех активных рецептов с отметкой о выводе на главной
    recipe_main_page = CardRecipe.objects.filter(display_main_page=True, is_active=True).order_by('add_datetime')

    content = {
        'shops': shops,
        'data_page': data_page,
        'catalog_active': catalog_active,
        'recipe_main_page': recipe_main_page,
    }
    return render(request, 'main/index.html', content)


def shop(request, shop_name):
    # выводим страницу магазина по name
    data_page = get_object_or_404(Shops, name=shop_name)

    if data_page.is_active:
        # загружает магазины для меню
        shops = get_shops_menu()

        # получаем все активные каталоги магазина
        card_active = Catalog.objects.filter(shop=data_page.pk, is_active=True).order_by('add_datetime')

        content = {
            'data_page': data_page,
            'shops': shops,
            'card_active': card_active,
            'breadcrumb_shop': True,
        }
    else:
        return HttpResponseRedirect(reverse('main:index'))

    return render(request, 'main/shop.html', content)


def catalog_page(request, shop_name, catalog_name):
    # выводит каталог по id
    data_page = get_object_or_404(Catalog, name=catalog_name)

    if data_page.is_active:
        # загружает магазины для меню
        shops = get_shops_menu()

        # получаем все активные картинки для открытого каталога
        picture = PictureCatalog.objects.filter(catalog__pk=data_page.pk, is_active=True).order_by('image_alt')

        # получаем все активные каталоги магазина
        card_active = Catalog.objects.filter(shop=data_page.shop, is_active=True).order_by('add_datetime')

        content = {
            'shops': shops,
            'data_page': data_page,
            'picture': picture,
            'card_active': card_active,
        }
    else:
        card_active = Catalog.objects.get(shop=data_page.shop, category=data_page.category, is_active=True)
        return HttpResponseRedirect(reverse('main:catalog_page', args=(card_active.pk,)))

    return render(request, 'main/catalog.html', content)
