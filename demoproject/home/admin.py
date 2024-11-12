from django.contrib import admin

from home.models import Category, Product


# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_featured', 'show_in_frontend')
    list_filter = ('price', 'is_featured', 'show_in_frontend')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
