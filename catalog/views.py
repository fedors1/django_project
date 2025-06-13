from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    if request.method == "GET":
        return render(request, "catalogs/home.html")
    return HttpResponse("YES")


def contacts(request):
    if request.method == "GET":
        return render(request, "catalogs/contacts.html")
    return HttpResponse("YES")


def products_list(request):
    products = Product.objects.all()
    context = {"products": products}
    return render(request, "catalogs/products_list.html", context)


def product_detail(request, pk):
    product = Product.objects.get(pk=pk)
    context = {"product": product}
    return render(request, "catalogs/product_detail.html", context)