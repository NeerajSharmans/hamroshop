from django.contrib import admin
from .models import *
# Register your models here.

from django.contrib import admin

class ProductHasImagesInline(admin.TabularInline):
    model = ProductHasImages

class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductHasImagesInline,
    ]

admin.site.register(Menu)
admin.site.register(Category)
admin.site.register(Banner)
admin.site.register(Product,ProductAdmin)