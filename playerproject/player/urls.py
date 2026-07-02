from django.urls import path
from player.views import home,welcome,add,update,dlt

urlpatterns=[
    path('',home,name='home'),
    path('welcome/',welcome,name='welcome'),
    path('add/',add,name='add'),
    path('edit/<int:id>/',update,name='edit'),
    path('dlt/<int:id>/',dlt,name='dlt'),
]