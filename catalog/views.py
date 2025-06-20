from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.models import Product
from forms import ProductForm


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


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogs/product_create.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:products_list")


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogs/product_create.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(DeleteView):
    model = Product
    template_name = "catalogs/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
