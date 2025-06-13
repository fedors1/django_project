from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.home, name="home"),
    path("contacts/", views.contacts, name="contacts"),
    path("products_list/", views.products_list, name="products_list"),
    path("product/<int:pk>/", views.product_detail, name="product_detail"),
]
