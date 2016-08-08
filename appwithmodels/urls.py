from django.conf.urls import url, include
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'home/',views.home),
    url(r'mobiles/',views.mobile_list),
    url(r'electronics/',views.electronics_list),
    url(r'addpost/',views.addpost),

]