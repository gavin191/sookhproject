from django.contrib import admin
from appwithmodels.models import Cars_sub_category, Furniture,Mobiles_sub_category 
# Register your models here.
admin.site.register(Cars_sub_category)
admin.site.register(Furniture)
admin.site.register(Mobiles_sub_category)
