from django.shortcuts import render
from .models import Category, Product, RestaurantInfo


def home(request):

    categories = Category.objects.all()

    products = Product.objects.filter(
        is_available=True
    ).select_related("category")

    restaurant = RestaurantInfo.objects.first()

    context = {
        "categories": categories,
        "products": products,
        "restaurant": restaurant,
    }

    return render(
        request,
        "menu/home.html",
        context
    )