from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect 
from appwithmodels.forms import Cars_sub_category_form
from django.core.urlresolvers import reverse
from appwithmodels.models import Cars_sub_category

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
        selector = request.POST.get("selector", "")
        title = request.POST.get("title", "")
        print(selector)
        print(title)
        if(selector=="Cars_sub_category"):
            form = Cars_sub_category_form(request.POST)
            if form.is_valid():
                print("in form valid")
                form.save()
                print('title=' + form.title)
                new_cars_sub_category_object = Cars_sub_category.create(title=form.title,price= form.price,description= form.description, photo = form.photo, name = form.name, phone_number = form.phone_number, city =form.city, cars_brand_name=form.cars_brand_name, cars_model = form.cars_model, kilometers_driven = form.kilometers_driven, year_manufacture =form.year_manufacture, fuel=form.fuel)
                new_cars_sub_category_object.save()
                print("in form valid")
                return HttpResponseRedirect(reverse('/sookh/addpost/'))
            else:
                print("form invalid")
                return render(request, 'addpost.html')
    else:
        return render(request, 'addpost.html')

