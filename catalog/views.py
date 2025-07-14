from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseForbidden
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    TemplateView,
    UpdateView,
    View,
)

from catalog.forms import ProductForm
from catalog.models import Product


class DeleteProductView(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if not request.user.has_perm("catalog.can_remove_product"):
            return HttpResponseForbidden(
                "У вас недостаточно прав для удаления продукта!"
            )
        elif request.user != product.owner:
            return Http404(
                "Вы не можете удалить продукт, потому что не являетесь его владельцем!"
            )

        product.delete()
        return redirect("catalog:product_list")


class ChangeProductStatusPublication(LoginRequiredMixin, View):
    def post(self, request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        if not request.user.has_perm("catalog.can_unpublish_product"):
            return HttpResponseForbidden(
                "У вас недостаточно прав для изменения статуса публикации продукта!"
            )
        elif request.user != product.owner:
            return Http404(
                "Вы не можете изменить статус публикации продукта, потому что не являетесь его владельцем!"
            )

        product.check_status = not product.check_status
        product.save()
        return redirect("catalog:product_update")


class HomeView(TemplateView):
    template_name = "catalogs/home.html"


class ContactsView(TemplateView):
    template_name = "catalogs/contacts.html"


class ProductsListView(ListView):
    model = Product
    template_name = "catalogs/products_list.html"
    context_object_name = "products"


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
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = "catalogs/product_create.html"
    context_object_name = "product"

    def get_success_url(self):
        return reverse("catalog:product_detail", args=[self.kwargs.get("pk")])


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    template_name = "catalogs/product_confirm_delete.html"
    success_url = reverse_lazy("catalog:products_list")
