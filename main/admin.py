from django.contrib import admin
from .models import Catalog, Shops, PictureCatalog, ArticlesCatalog

admin.site.register(Catalog)
admin.site.register(Shops)
admin.site.register(PictureCatalog)
admin.site.register(ArticlesCatalog)
