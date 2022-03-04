from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('add-customer/', views.addCustomer, name='add-customer'),
    path('edit-customer/<str:pk>/', views.editCustomer, name='edit-customer'),
    path('delete-customer/<str:pk>/', views.deleteCustomer, name='delete-customer'),
    path('search/', views.searchCustomer, name='search'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
]
