from django.db import models
from django_resized import ResizedImageField


class ArticlesCatalog(models.Model):
    WEEK = 'week'
    MONTH = 'month'
    SPECIAL = 'special'
    PAGE = 'page'
    CATEGORY_CHOICES = (
        (WEEK, 'week'),
        (MONTH, 'month'),
        (SPECIAL, 'special'),
        (PAGE, 'page'),
    )

    category = models.CharField(verbose_name='категория каталога текста', max_length=10, blank=True, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    h2_title = models.TextField(verbose_name='заголовок статьи (текста)', blank=True)
    article = models.TextField(verbose_name='статья', blank=True)
    comment = models.CharField(verbose_name='комментарий', max_length=250, blank=True)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'(id {self.pk} - {self.category}) {self.h2_title}'


class Shops(models.Model):
    MAIN = 'main'
    SHOP = 'shop'
    CATEGORY_CHOICES = (
        (MAIN, 'main'),
        (SHOP, 'shop'),
    )
    name = models.CharField(verbose_name='название магазина (переменная в коде!)', max_length=64, unique=True)
    article_catalog = models.ForeignKey(ArticlesCatalog, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    is_menu = models.BooleanField(verbose_name='выводить в меню', default=False)
    category_page = models.CharField(verbose_name='категория страницы (главная или магазин)', max_length=10, blank=True, choices=CATEGORY_CHOICES)
    title_shop = models.CharField(verbose_name='сокр название', max_length=64, blank=True)
    title_shop_full = models.CharField(verbose_name='полное название', max_length=64, blank=True)
    meta_title = models.CharField(verbose_name='meta title', max_length=250, blank=True)
    h1_title = models.CharField(verbose_name='title H1', max_length=250, blank=True)
    meta_description = models.TextField(verbose_name='meta description', blank=True)
    alt_shop = models.CharField(verbose_name='alt логотипа', max_length=64, blank=True)
    image_logo = models.FileField(upload_to='logo_images', verbose_name='логотип', blank=True)
    image_preview = models.ImageField(upload_to='previews_images/%Y/%m/%d/', verbose_name='картинка для шаринга (meta og:image)', blank=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'id {self.pk} - {self.name}'


class Catalog(models.Model):
    WEEK = 'week'
    MONTH = 'month'
    SPECIAL = 'special'
    CATEGORY_CHOICES = (
        (WEEK, 'week'),
        (MONTH, 'month'),
        (SPECIAL, 'special'),
    )

    shop = models.ForeignKey(Shops, on_delete=models.SET_NULL, null=True)
    article_catalog = models.ForeignKey(ArticlesCatalog, on_delete=models.SET_NULL, null=True)
    category = models.CharField(verbose_name='категория каталога', max_length=10,  blank=True, choices=CATEGORY_CHOICES)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    display_main_page = models.BooleanField(verbose_name='выводить каталог на главной странице', default=False)
    name = models.CharField(verbose_name='имя каталога', max_length=128)
    short_desc = models.CharField(verbose_name='краткое описание каталога', max_length=128, blank=True)
    breadcrumb_title = models.CharField(verbose_name='breadcrumb', max_length=128, blank=True)
    meta_title = models.CharField(verbose_name='meta title', max_length=250, blank=True)
    h1_title = models.CharField(verbose_name='title H1', max_length=250, blank=True)
    muted_title = models.CharField(verbose_name='title серый под H1', max_length=250, blank=True)
    meta_description = models.TextField(verbose_name='meta description', blank=True)
    image_preview = models.ImageField(upload_to='previews_images/%Y/%m/%d/', blank=True)
    card_image_alt_a_title = models.CharField(verbose_name='card title_alt (картинки и ссылки)', max_length=250, blank=True)
    card_title = models.CharField(verbose_name='card название каталога (видимый текст)', max_length=250, blank=True)
    card_date = models.CharField(verbose_name='card срок действия каталога', max_length=50, blank=True)
    add_datetime = models.DateTimeField(verbose_name='время добавления',  auto_now_add=True)
    update_date = models.DateTimeField(verbose_name='время обновления', auto_now=True)

    def __str__(self):
        return f'id {self.pk} - {self.name} ({self.shop.name})'


class PictureCatalog(models.Model):
    catalog = models.ForeignKey(Catalog, on_delete=models.SET_NULL, null=True)
    is_active = models.BooleanField(verbose_name='активный / действующий', default=True)
    image = models.ImageField(upload_to='catalogs_images/%Y/%m/%d/', blank=True)
    image_resized = ResizedImageField(upload_to='catalogs_images/%Y/%m/%d/', blank=True)
    image_alt = models.PositiveSmallIntegerField(verbose_name='номер страницы каталога', default=0)
    add_datetime = models.DateTimeField(verbose_name='время добавления', auto_now_add=True)

    def __str__(self):
        return f'(id {self.catalog.pk} - {self.catalog.name}) стр. {self.image_alt}'
