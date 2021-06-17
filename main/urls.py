from django.urls import path
from django.views.generic.base import TemplateView
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('<slug:shop_name>', views.shop, name='shop'),
    path('<slug:shop_name>/<slug:catalog_name>', views.catalog_page, name='catalog_page'),
]