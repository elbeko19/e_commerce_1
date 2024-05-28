from django.urls import path, include
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.all_products),
    path('search/all', views.all_products),
    path('item/<slug:slug>', views.product_detail, name='product_detail'),
    path('search/<slug:category_slug>', views.categories_list, name='categories_list'),
]
