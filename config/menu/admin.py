from django.contrib import admin
from .models import Category, Product, RestaurantInfo


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "category",
        "price",
        "is_available",
        "created_at",
    )

    list_filter = (
        "category",
        "is_available",
    )

    search_fields = (
        "name",
        "description",
    )

    list_editable = (
        "price",
        "is_available",
    )


@admin.register(RestaurantInfo)
class RestaurantInfoAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "phone",
    )