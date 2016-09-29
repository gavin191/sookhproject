from django.conf.urls import url, include
from django.contrib import admin
from . import views 

urlpatterns = [
    url(r'home/',views.home),
    url(r'mobiles/',views.Mobiles_list),
    url(r'tablets/',views.Tablets_list),
    url(r'accessories/',views.Accessories_list),
    url(r'computer/',views.Computer_list),
    url(r'tvvideo/',views.Tv_video_list),
    url(r'camera/',views.Camera_list),
    url(r'games/',views.Games_list),
    url(r'fridgeacwashingmachine/',views.Fridge_ac_washingmachine_list),
    url(r'kitchen/',views.Kitchen_other_list),
    url(r'cars/',views.cars_list),
    url(r'commercial/',views.Commercial_vehicle_list),
    url(r'othervehicles/',views.Other_vehicles_list),
    url(r'sparecars/',views.Spare_parts_cars_list),
    url(r'motorcycles/',views.Motorcycles_list),
    url(r'bicycles/',views.Bicycles_sub_category_list),
    url(r'sparebikes/',views.Spare_parts_bikes_list),
    url(r'furniture/',views.Furniture_list),
    url(r'ip/',views.ip_list),
    url(r'addpost/',views.addpost),

]