from django.shortcuts import render
from dashboard.models import Barang, Transaksi, Costumer
from dashboard.forms import form_barang, form_transaksi, form_costumer

def produk(request):
    nama = 'Produk'
    konteks = {
        'title': nama,
    }
    return render(request, 'produk.html', konteks)

# Create your views here.


def tambah_barang(request):
    form = form_barang()
    konteks = {
        'form': form,
    }
    return render(request, 'tambah_barang.html', konteks)

def Barang_view(request):
    Barangs = Barang.objects.all()
    
    konteks={
        'Barangs': Barangs,
    }
    return render(request,'tampil_barang.html', konteks)

def transaksi_list(request):
    Transaksis = Transaksi.objects.all()
    konteks={
        'Transaksis' :Transaksis,
    }
    return render(request, 'transaksi_list.html', konteks)

def List_costumer(request):
    Customers = Costumer.objects.all()
    
    konteks={
        'Customers':Customers
    }
    return render(request, 'customer.html', konteks)
    
    
