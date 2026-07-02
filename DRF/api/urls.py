from django.urls import path 
from .views import home ,home1,home2
urlpatterns=[
    path('',home,name='home'),
    path('home1/',home1,name='home1'),
    path('home2/',home2,name='home2'),

]