from django.contrib import admin
from .models import Products,Order

class ProductAdmin(admin.ModelAdmin):

    def change_cateegory_to_default(self,request,queryset):
        queryset.update(category="default")

    list_display=('title','price','discounted_price','cateegory')
    search_fields=('title','cateegory')
    actions=('change_cateegory_to_default')

# Register your models here.
admin.site.register(Products,ProductAdmin)
admin.site.register(Order)
