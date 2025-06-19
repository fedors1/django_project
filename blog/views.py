from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from blog.models import Blog


class BlogList(ListView):
    model = Blog
    template_name = "blogs/blog_list.html"
    context_object_name = "blogs"

    def get_queryset(self):
        return Blog.objects.filter(is_active=True)



class BlogDetail(DetailView):
    model = Blog
    template_name = "blogs/blog_detail.html"
    context_object_name = "blog"

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.views_counter += 1
        obj.save()
        return obj


class BlogCreate(CreateView):
    model = Blog
    fields = ("header", "description", "preview")
    template_name = "blogs/blog_create.html"
    context_object_name = "blog"
    success_url = reverse_lazy("blog:blog_list")


class BlogUpdate(UpdateView):
    model = Blog
    fields = ("header", "description", "preview")
    template_name = "blogs/blog_create.html"
    context_object_name = "blog"

    def get_success_url(self):
        return reverse("blog:blog_detail", args=[self.kwargs.get("pk")])


class BlogDelete(DeleteView):
    model = Blog
    template_name = "blogs/blog_confirm_delete.html"
    success_url = reverse_lazy("blog:blog_list")
