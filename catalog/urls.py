from django.urls import path

from catalog.apps import CatalogConfig

from . import views

app_name = CatalogConfig.name

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("contacts/", views.ContactsView.as_view(), name="contacts"),
    path("products_list/", views.ProductsListView.as_view(), name="products_list"),
    path("product/<int:pk>/", views.ProductDetailView.as_view(), name="product_detail"),
    path("product/create/", views.ProductCreateView.as_view(), name="product_create"),
    path(
        "product/<int:pk>/update/",
        views.ProductUpdateView.as_view(),
        name="product_update",
    ),
    path(
        "product/<int:pk>/delete/",
        views.ProductDeleteView.as_view(),
        name="product_confirm_delete",
    ),
    path(
        "delete_my_product/<int:pk>/",
        views.DeleteProductView.as_view(),
        name="delete_my_product",
    ),
    path(
        "change_product_status/<int:pk>",
        views.ChangeProductStatusPublication.as_view(),
        name="change_product_status",
    ),
]
