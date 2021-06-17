from django.db import models


class Recipes(models.Model):
    name = models.CharField(verbose_name='url-название рецепта', max_length=250)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    main_image = models.ImageField(upload_to='kitchen/recipes/%Y/%m/%d/', verbose_name='главное фото рецепта', blank=True)
    main_image_alt_a_title = models.CharField(verbose_name='title_alt главного фото (картинки и ссылки)', max_length=250, blank=True)
    breadcrumb_title = models.CharField(verbose_name='breadcrumb', max_length=250, blank=True)
    meta_title = models.CharField(verbose_name='meta title', max_length=250, blank=True)
    h1_title = models.CharField(verbose_name='title H1', max_length=250, blank=True)
    meta_description = models.TextField(verbose_name='meta description', blank=True)
    ingredients = models.TextField(verbose_name='список ингредиентов', blank=True)
    introduction_description = models.TextField(verbose_name='вступление, текст описания перед шагами', blank=True)
    time_work = models.CharField(verbose_name='время приготовления', max_length=50, blank=True)
    portions = models.CharField(verbose_name='кол-во порций', max_length=50, blank=True)
    short_desc = models.CharField(verbose_name='краткое описание рецепта', max_length=250, blank=True)
    add_datetime = models.DateTimeField(verbose_name='время добавления',  auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'id {self.pk} - {self.h1_title}'


class CardRecipe(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    display_main_page = models.BooleanField(verbose_name='выводить карточку на главной странице', default=False)
    image_preview = models.ImageField(upload_to='kitchen/recipes/%Y/%m/%d/', verbose_name='image_preview', blank=True)
    card_image_alt_a_title = models.CharField(verbose_name='card title_alt (картинки и ссылки)', max_length=250, blank=True)
    card_title = models.CharField(verbose_name='card название рецепта (видимый текст)', max_length=250, blank=True)
    card_description = models.TextField(verbose_name='card описание рецепта', blank=True)
    time_work = models.CharField(verbose_name='время приготовления', max_length=50, blank=True)
    portions = models.CharField(verbose_name='кол-во порций', max_length=50, blank=True)
    add_datetime = models.DateTimeField(verbose_name='время добавления',  auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'id {self.pk} - {self.card_title}'


class ArticlesRecipes(models.Model):
    recipe = models.ForeignKey(Recipes, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    step = models.PositiveSmallIntegerField(verbose_name='номер шага приготовления', default=1)
    step_image = models.ImageField(upload_to='kitchen/recipes/%Y/%m/%d/', verbose_name='фото', blank=True)
    step_image_alt_a_title = models.CharField(verbose_name='step title_alt (картинки и ссылки)', max_length=250, blank=True)
    step_description = models.TextField(verbose_name='описание', blank=True)
    add_datetime = models.DateTimeField(verbose_name='время добавления',  auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'id {self.pk} - {self.step} ({self.recipe.h1_title})'


