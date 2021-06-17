from django.urls import path

import kitchenapp.views as kitchenapp

app_name = 'kitchenapp'

urlpatterns = [
    path('recipes', kitchenapp.recipes_all, name='recipes_all'),
    path('recipes/<slug:recipe_name>', kitchenapp.recipes, name='recipes'),

]
