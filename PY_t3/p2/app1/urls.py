from django.urls import path
from app1.views import Home
from app1.views import About
# from.import About
urlpatterns= [
    path('home/',Home,name='home'),
    path('about/',About,name='about')
]