from django.urls import path
from blog.apps import BlogConfig
from . import views

app_name = BlogConfig.name


urlpatterns = [
    path("blog_list/", views.BlogList.as_view(), name="blog_list"),
    path("blog/<int:pk>/", views.BlogDetail.as_view(), name="blog_detail"),
    path("blog/create/", views.BlogCreate.as_view(), name="blog_create"),
    path("blog/<int:pk>/update/", views.BlogUpdate.as_view(), name="blog_update"),
    path("blog/<int:pk>/delete/", views.BlogDelete.as_view(), name="blog_confirm_delete"),
]