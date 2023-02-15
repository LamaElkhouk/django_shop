from django.contrib import admin
from api.models import Category, Product
# Register your models here.


class CategoryAdmin(admin.ModelAdmin):

    list_display = ('nom', 'description', 'active')


class ProductAdmin(admin.ModelAdmin):

    list_display = ('nom', 'description', 'prix',
                    'image', 'category', 'active')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
