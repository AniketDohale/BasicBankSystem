from django.contrib import admin
from django.urls import path, include
from Bank import views

urlpatterns = [
    path('', views.index, name='intro'),
    path("home", views.home, name='home'),
    path("customers", views.customers, name='customers'),
    path("about", views.about, name='abput'),
    path("contact", views.contact, name='contact'),
    path("payment/<str:cust_id>", views.payment, name='payment'),
    path("trans_history", views.trans_history, name='trans_history'),
]
