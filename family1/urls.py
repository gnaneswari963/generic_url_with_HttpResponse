from family1.views import *
from django.urls import path
app_name="something"
urlpatterns=[
    path('gnaneswari/',gnaneswari,name='gnaneswari'),
    path('hari/',hari,name='hari')
]