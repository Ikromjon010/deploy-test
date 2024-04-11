from django.urls import path
from .views import mahsulot_list_view, maxsulot_batafsil_view


urlpatterns = [
    path('mahsulot/', mahsulot_list_view, name = 'all_products'),


    path('mahsulot/<int:id>/', maxsulot_batafsil_view, name = 'product_detail'),
]
