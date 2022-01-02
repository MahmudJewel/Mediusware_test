from django.urls import path, include
from product import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search', views.search_view, name='search'),
    path('add', views.add_product_view, name='add'),
    path('edit/<int:pk>', views.edit_product, name='edit')
]