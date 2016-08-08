from django.db import models

# Create your models here.
#modile category section
class Mobiles(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)

    class  Meta:
        abstract = True

class Mobiles_sub_category(Mobiles):
    mobile_brand_name= models.CharField(max_length=250)

class Tablets_sub_category(Mobiles):
    tablets_brand_name =models.CharField(max_length=250)

class Accessories_sub_category(Mobiles):
    mobile_accessory_choice_mobile = models.BooleanField()
    mobile_accessory_choice_tablet = models.BooleanField()
    accessory_brand_name =models.CharField(max_length=250)

#electronics section
class Electronics(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)

    class  Meta:
        abstract = True

class Computer_sub_category(Electronics):
    computer_item_sub_category= models.CharField(max_length=250)
    computer_brand_name = models.CharField(max_length=250)

class Tv_video_sub_category(Electronics):
    tv_video_sub_category=models.CharField(max_length=250)

class Camera_sub_category(Electronics):
    camera_item_sub_category=models.CharField(max_length=250)

class Games_sub_category(Electronics):
    Games_item_sub_category=models.CharField(max_length=250)

class Fridge_ac_washingmachine(Electronics):
    Fridge_ac_washingmachine_sub_category=models.CharField(max_length=250)

class Kitchen_other(Electronics):
    Kitchen_other_sub_category=models.CharField(max_length=250)

# cars section

class Cars(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)

    class  Meta:
        abstract = True

class Cars_sub_category(Cars):
    cars_brand_name = models.CharField(max_length=250)
    cars_model = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.DateField()
    fuel = models.CharField(max_length=250)

class Commercial_vehicle_sub_category(Cars):
    commercial_vehicle_brand_name = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.DateField()
    fuel = models.CharField(max_length=250)

class Other_vehicles_sub_category(Cars):
    Other_vehicles_brand_name = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.DateField()
    fuel = models.CharField(max_length=250)    

class Spare_parts_cars_sub_category(Cars):
    spare_parts_category = models.CharField(max_length=250)

class Bikes(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)

    class  Meta:
        abstract = True


class Motercycles_sub_category(Bikes):
    motorc_brand_name = models.CharField(max_length=250)
    bikes_model = models.CharField(max_length=250)
    kilometers_driven = models.IntegerField()
    year_manufacture = models.DateField()
    fuel = models.CharField(max_length=250)

class Bicycles_sub_category(Bikes):
    bicycle_brand_name = models.CharField(max_length=250)

class Spare_parts_bikes_sub_category(Bikes):
    spare_bikes_name = models.CharField(max_length=250)

class Furniture(models.Model):
    title = models.CharField(max_length=250)
    price = models.IntegerField()
    furniture_type = models.CharField(max_length=250)
    description=models.TextField()
    photo = models.ImageField()
    name = models.CharField(max_length=250)
    phone_number = models.IntegerField()
    city = models.CharField(max_length=250)














