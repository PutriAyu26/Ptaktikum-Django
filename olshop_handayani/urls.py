"""olshop_handayani URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from pathlib import Path
from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.shortcuts import render
from dashboard.views import produk, tambah_barang, Barang_view, transaksi_list, List_costumer

def home(request):
    nama = 'Home'
    konteks = {
        'title': nama,
    }
    return render(request, 'home.html', konteks)


urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', home, name='home'),
    path('produk/', produk, name='produk'),
    path('addbrg/', tambah_barang, name='addbrg'),
    path('brgview/', Barang_view, name='brgview'),
    path("transaksi/", transaksi_list, name='transaksi'),
    path("costumer/", List_costumer, name='costumer'),
]
