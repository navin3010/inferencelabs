from django.urls import path
from ecom import views

urlpatterns = [
    path("category/", views.CategoryAPI.as_view(), name = "Create category"),
    path("products/", views.ProductsAPI.as_view(), name = "Products details"),
    path("review/", views.review, name = "Products review")
]