from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.first, name = 'first'),
    path('second/', views.second, name = 'second'),
    path('accounts/', views.accounts, name = 'accounts'),
    path('blog/', views.blog, name = 'blog'),
    path('login/', views.login, name = 'login'),
]