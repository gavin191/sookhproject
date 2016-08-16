from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from appwithmodels.forms import Cars_sub_category_form,FurnitureForm
from django.core.urlresolvers import reverse
from appwithmodels.models import Cars_sub_category,Furniture


# Create your views here.

def mobile_list(request):
    '''function in view    '''
    documents={}
    documents = Mobiles.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documents,}
    )

def electronics_list(request):
    '''function in view    '''
    documents={}
    documents = Electronics.objects.all()

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documents,}
    )

def home(request):
    return render(request,'home.html')

@csrf_protect
def addpost(request):
    print("in addpost")
    if request.method == 'POST':
        subcategories = subcategoriesview = request.POST.get("subcategories", "")
        print('subcategories' + subcategories)
        if(subcategories=='car'):
            form = Cars_sub_category_form(request.POST,request.FILES)
            if form.is_valid():
                print("in form valid")
                titleview = request.POST.get("title", "")
                photoview = request.POST.get("price", "")
                subcategoriesview = request.POST.get("subcategories", "")
                priceview = request.POST.get("price", "")
                descriptionview = request.POST.get("description", "")
                nameview = request.POST.get("name", "")
                phone_numberview = request.POST.get("phone_number", "")
                cityview = request.POST.get("city", "")
                cars_brand_nameview = request.POST.get("cars_brand_name", "")
                cars_modelview = request.POST.get("cars_model", "")
                kilometers_drivenview = request.POST.get("kilometers_driven", "")
                year_manufactureview = request.POST.get("year_manufacture", "")
                fuelview = request.POST.get("fuel", "")
                categoriesview = request.POST.get("categories", "")
                new_cars_sub_category_object = Cars_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,cars_brand_name=cars_brand_nameview
                ,cars_model=cars_modelview
                ,kilometers_driven=kilometers_drivenview
                ,year_manufacture=year_manufactureview
                ,fuel=fuelview
                ,categories=categoriesview)
                new_cars_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid")
                return render(request, 'addpost.html')
        elif(subcategories=='furniture'):
            form = FurnitureForm()
            titleview = request.POST.get("title", "")
            photoview = request.POST.get("price", "")
            subcategoriesview = request.POST.get("subcategories", "")
            priceview = request.POST.get("price", "")
            descriptionview = request.POST.get("description", "")
            nameview = request.POST.get("name", "")
            phone_numberview = request.POST.get("phone_number", "")
            cityview = request.POST.get("city", "")
            categoriesview = request.POST.get("categories", "")
            furniture_typeview = request.POST.get("furniture_type", "")
            print(subcategoriesview, titleview, priceview, descriptionview ,nameview, cityview, categoriesview ,furniture_typeview)
            form = FurnitureForm(request.POST,request.FILES)
            if form.is_valid():
                print("in form valid")
                
                titleview = request.POST.get("title", "")
                photoview = request.POST.get("price", "")
                subcategoriesview = request.POST.get("subcategories", "")
                priceview = request.POST.get("price", "")
                descriptionview = request.POST.get("description", "")
                nameview = request.POST.get("name", "")
                phone_numberview = request.POST.get("phone_number", "")
                cityview = request.POST.get("city", "")
                categoriesview = request.POST.get("categories", "")
                furniture_typeview = request.POST.get("furniture_type", "")

                new_furnitureobject = Furniture(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview,
                name=nameview,
                phone_number=phone_numberview,
                city=cityview,
                furniture_type=furniture_typeview,
                categories=categoriesview)

                new_furnitureobject.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid")
                return render(request, 'addpost.html')
    else:
        return render(request, 'addpost.html',)
