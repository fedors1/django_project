from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.cache import cache
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
)

from catalog.forms import ProductForm
from catalog.models import Product, Category
from catalog.services import ProductService


class HomeView(TemplateView):
    template_name = "catalogs/home.html"


class ContactsView(TemplateView):
    template_name = "catalogs/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = "catalogs/products_list.html"
    context_object_name = "products"

    def get_queryset(self):
        return Product.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):

        context = super().get_context_data(**kwargs)
        context["categories"] = Category.objects.all()
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductsByCategoryListView(ListView):
    model = Product
    template_name = "catalogs/products_by_category.html"
    context_object_name = "products"

    def get_queryset(self):
        category_id = self.kwargs.get("category_id")
        return ProductService.return_list_products(category_id)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["category"] = get_object_or_404(Category, id=self.kwargs.get("category_id"))
        return context


@method_decorator(cache_page(60 * 15), name="dispatch")
class ProductDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalogs/product_detail.html"
    context_object_name = "product"


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogs/product_create.html"
    context_object_name = "product"
    success_url = reverse_lazy("catalog:products_list")

    def form_valid(self, form):
        form.instance.owner = self.request.user
        form.instance.category = self.request.category_id
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogs/product_create.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if (
            not request.user.has_perm("catalog.can_unpublish_product")
            or request.user != product.owner
        ):
            return HttpResponseForbidden(
                "У вас недостаточно прав для изменения статуса публикации продукта!"
            )

        product.check_status = not product.check_status
        product.save()
        return redirect("catalog:product_detail")


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalogs/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")

    def post(self, request, *args, **kwargs):
        product = self.get_object()
        if (
            not request.user.has_perm("catalog.can_remove_product")
            or request.user != product.owner
        ):
            return HttpResponseForbidden(
                "У вас недостаточно прав для удаления продукта!"
            )

        return super().post(*args, **kwargs)
