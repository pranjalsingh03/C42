"""C42 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('products/', prod, name='products'),
    path('addproducts/', addprods, name='addproducts'),
    path('edit_product/', edit_prod, name='editproduct'),
    path('plustock/', plustock, name='plustock'),
    path('minustock/', minustock, name='minustock'),
    path('note/', note, name='note'),
    path('invoice_list/', invoice_list, name='invoice_list'),
    path('invoice_create/', invoice_create, name='invoice_create'),
    path('invoice_ready/', gen_invoice, name='invoice_gen'),
    path('staf/', stafs, name='staf'),
    path('pay_history/', pay_history, name='pay_history'),
    path('Records/', record, name='report'),
    path('clear_cart/', clear_cart, name='clear_cart'),
    path('sale_history/', sale_history, name='sale_history'),
    path('invoice__prod_collect/', invoice_collect, name='inv_prod'),
    path('invoice_cart_update/', invoice_cart_update, name='invoice_cart_update'),
    path('backup/', backup, name='backup')

]
