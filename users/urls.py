from django.urls import path
from users import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
    path(
        "password-reset/",
        views.password_reset,
        name="Reset password",
    ),
]