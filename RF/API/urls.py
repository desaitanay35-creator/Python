from django.urls import path
from .views import api_demo,api_detail

urlpatterns=[
    path('',api_demo,name='api_demo'),
    path('api_detail/<int:id>/',api_detail,name='api_detail')
]
