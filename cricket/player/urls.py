from django.urls import path
from player.views import home,about,navebar,info
urlpatterns=[
    path('',home,name='home1'),
    path('about/',about,name='about1'),
    path('',navebar),
    path('info/<int:id>',info,name='info1')
    


]