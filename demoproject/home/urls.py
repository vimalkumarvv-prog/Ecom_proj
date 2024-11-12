from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home'),
    path('add_product/', views.add_product, name='add_product'),
    path('edit_product/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete_product/<int:product_id>/', views.delete_product, name='delete_product'),
    path('signup/', views.signup, name='signup'),
    path('signin/', views.signin, name='signin'),
    path('signout/', views.signout, name='signout'),
    path('user_dashboard/', views.user_dashboard, name='user_dashboard'),
    path('featured_products', views.featured_products_view, name='featured_products_view'),
]
