from django.urls import path
from app2.views import Contect,base

urlpatterns= [
    path('contect/',Contect,name='contect'),
    path('base/',base)
]