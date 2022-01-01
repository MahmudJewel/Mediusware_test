from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.home_view, name='home'),
]