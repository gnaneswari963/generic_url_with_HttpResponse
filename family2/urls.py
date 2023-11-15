from family2.views import *
from django.urls import path
app_name='anything'
urlpatterns=[
    path('nani',nani,name='nani'),
    path('gnaneswari',gnaneswari,name='gnaneswari'),
]