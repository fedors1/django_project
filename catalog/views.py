from django.views.generic import DetailView, ListView, TemplateView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = "catalogs/home.html"


class ContactsView(TemplateView):
    template_name = "catalogs/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = "catalogs/products_list.html"
    context_object_name = "products"


class ProductDetailView(DetailView):
    model = Product
    template_name = "catalogs/product_detail.html"
    context_object_name = "product"
