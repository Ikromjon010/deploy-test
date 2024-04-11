from django.shortcuts import render
from .models import Mahsulot

# Create your views here.



def mahsulot_list_view(request):
    mahsulot_jami = Mahsulot.objects.all() # select * from mahsulot;

    context = {
        'products_all' : mahsulot_jami
    }

    return render(request, 'jami_mahsulot.html', context)



def maxsulot_batafsil_view(request, id):

    detail = Mahsulot.objects.get(id = id)

    context = {
        'product': detail
    }
    return render(request, 'mahsulot.html', context)
