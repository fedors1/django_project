from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("products_list/", views.ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
]
