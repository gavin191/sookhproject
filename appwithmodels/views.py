from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.views.decorators.csrf import csrf_protect
from appwithmodels.forms import Cars_sub_category_form,Furniture_Form,Mobile_sub_MobileForm,Mobile_sub_tablets_form,Mobile_sub_accessories_form,Computer_sub_category_form,Tv_video_sub_category_form,Camera_sub_category_form,Games_sub_category_form,Fridge_ac_washingmachine_form,Kitchen_other_form,Cars_sub_category_form,Commercial_vehicle_sub_category_form,Other_vehicles_sub_category_form,Spare_parts_cars_sub_category_form,Motorcycles_sub_category_form,Bicycles_sub_category_form,Spare_parts_bikes_sub_category_form,Furniture_Form
from django.core.urlresolvers import reverse
from appwithmodels.models import Cars_sub_category,Furniture,Mobiles_sub_category,Tablets_sub_category,Accessories_sub_category,Computer_sub_category,Tv_video_sub_category,Camera_sub_category,Games_sub_category,Fridge_ac_washingmachine,Kitchen_other,Cars_sub_category,Commercial_vehicle_sub_category,Other_vehicles_sub_category,Spare_parts_cars_sub_category,Motorcycles_sub_category,Bicycles_sub_category,Spare_parts_bikes_sub_category,Furniture
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from haystack.query import SearchQuerySet

# Create your views here.
def ip_list(request):
    a=get_ip(request)
    print("ip is" + a)

@csrf_protect
def search_list(request):
    print("in search")
    if request.method == 'POST':
        searchdata = request.POST.get("search", "")
        print(searchdata)
        all_results = SearchQuerySet().filter(content=searchdata)
        print(all_results)
        paginator = Paginator(all_results, 5) # Show 25 contacts per page
        page = request.GET.get('page')
        try:
            documentspage = paginator.page(page)
        except PageNotAnInteger:
                # If page is not an integer, deliver first page.
                documentspage = paginator.page(1)
        except EmptyPage:
            # If page is out of range (e.g. 9999), deliver last page of results.
            documentspage = paginator.page(paginator.num_pages)
        return render(
            request,
            'home.html',
            {'documents': documentspage,}
        )
    else:
        return render(request, 'home.html',)




@csrf_protect
def Mobiles_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Mobiles_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Mobiles_sub_category.objects.filter(price__gte=min)
    else:
        documents = Mobiles_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/mobiles/'}
    )

def Tablets_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Tablets_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Tablets_sub_category.objects.filter(price__gte=min)
    else:
        documents = Tablets_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'//sookh/tablets/'}
    )

def Accessories_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Accessories_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Accessories_sub_category.objects.filter(price__gte=min)
    else:
        documents = Accessories_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/accessories/'}
    )

def Computer_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Computer_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Computer_sub_category.objects.filter(price__gte=min)
    else:
        documents = Computer_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/computer/'}
    )

def Tv_video_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Tv_video_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Tv_video_sub_category.objects.filter(price__gte=min)
    else:
        documents = Tv_video_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/tvvideo/'}
    )

def Camera_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Camera_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Camera_sub_category.objects.filter(price__gte=min)
    else:
        documents = Camera_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/camera/'}
    )

def Games_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Games_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Games_sub_category.objects.filter(price__gte=min)
    else:
        documents = Games_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/games/'}
    )

def Fridge_ac_washingmachine_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Fridge_ac_washingmachine.objects.filter(price__range=(min, max))
        else:
            documents = Fridge_ac_washingmachine.objects.filter(price__gte=min)
    else:
        documents = Fridge_ac_washingmachine.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/fridgeacwashingmachine/'}
    )

def Kitchen_other_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Kitchen_other.objects.filter(price__range=(min, max))
        else:
            documents = Kitchen_other.objects.filter(price__gte=min)
    else:
        documents = Kitchen_other.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/kitchen/'}
    )

def Commercial_vehicle_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Commercial_vehicle_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Commercial_vehicle_sub_category.objects.filter(price__gte=min)
    else:
        documents = Commercial_vehicle_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/commercial/'}
    )

def Other_vehicles_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Other_vehicles_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Other_vehicles_sub_category.objects.filter(price__gte=min)
    else:
        documents = Other_vehicles_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/othervehicles/'}
    )

def Spare_parts_cars_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Spare_parts_cars_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Spare_parts_cars_sub_category.objects.filter(price__gte=min)
    else:
        documents = Spare_parts_cars_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

 
    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/sparecars/'}
    )

def Motorcycles_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Motorcycles_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Motorcycles_sub_category.objects.filter(price__gte=min)
    else:
        documents = Motorcycles_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/motorcycles/'}
    )

def Bicycles_sub_category_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Bicycles_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Bicycles_sub_category.objects.filter(price__gte=min)
    else:
        documents = Bicycles_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')

    documents = Bicycles_sub_category.objects.all()
    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/bicycles/'}
    )

def Spare_parts_bikes_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Spare_parts_bikes_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Spare_parts_bikes_sub_category.objects.filter(price__gte=min)
    else:
        documents = Spare_parts_bikes_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/sparebikes/'}
    )

def Furniture_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Furniture.objects.filter(price__range=(min, max))
        else:
            documents = Furniture.objects.filter(price__gte=min)
    else:
        documents = Furniture.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/furniture/'}
    )




def cars_list(request):
    '''function in view    '''
    documents={}
    min=request.POST.get("price_min", "")
    max=request.POST.get("price_max", "")
    minmax=request.POST.get("minmax", "")
    if(min!=''):
        if(max!=''):
            documents = Cars_sub_category.objects.filter(price__range=(min, max))
        else:
            documents = Cars_sub_category.objects.filter(price__gte=min)
    else:
        documents = Cars_sub_category.objects.all()
    if(minmax=='lowtohigh'):
        documents=  documents.order_by('price')
    elif(minmax=='hightolow'):
        documents= documents.order_by('-price')


    paginator = Paginator(documents, 5) # Show 25 contacts per page

    page = request.GET.get('page')
    try:
        documentspage = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        documentspage = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        documentspage = paginator.page(paginator.num_pages)

    # Render list page with the documents and the form
    return render(
        request,
        'displaydocuments.html',
        {'documents': documentspage,'urls':'/sookh/cars/'}
    )





def home(request):
    return render(request,'home.html')

@csrf_protect
def addpost(request):
    print("in addpost")
    if request.method == 'POST':
        print("in post if")
    else:
        print("not in post if"+ request.method)
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
        elif(subcategories=='mobiles'):
            form = Mobile_sub_MobileForm(request.POST,request.FILES)
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
                mobile_brand_nameview=request.POST.get("mobile_brand_name", "")
                new_Mobiles_sub_category_object = Mobiles_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,mobile_brand_name=mobile_brand_nameview
                ,categories=categoriesview)
                new_Mobiles_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid")
                return render(request, 'addpost.html')

        elif(subcategories=='tablets'):
            form = Mobile_sub_tablets_form(request.POST,request.FILES)
            print(form)
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
                tablet_brand_nameview=request.POST.get("tablet_brand_name", "")
                new_Tablets_sub_category_object = Tablets_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,tablets_brand_name=tablet_brand_nameview
                ,categories=categoriesview)
                new_Tablets_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for tablets")
                return render(request, 'addpost.html')

        elif(subcategories=='accessories'):
            form = Mobile_sub_accessories_form(request.POST,request.FILES)
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
                mobile_accessory_choiceview=request.POST.get("mobile_accessory_choice", "")
                accessory_brand_nameview=request.POST.get("accessory_brand_name", "")
                new_Accessories_sub_category_object = Accessories_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,mobile_accessory_choice=mobile_accessory_choiceview
                ,accessory_brand_name=accessory_brand_nameview
                ,categories=categoriesview)
                new_Accessories_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid")
                return render(request, 'addpost.html')

        elif(subcategories=='computer'):
            form = Computer_sub_category_form(request.POST,request.FILES)
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
                computer_item_sub_categoryview=request.POST.get("computer_item_sub_category", "")
                computer_brand_nameview=request.POST.get("computer_brand_name", "")
                new_Computer_sub_category_object = Computer_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,computer_item_sub_category=computer_item_sub_categoryview
                ,computer_brand_name=computer_brand_nameview
                ,categories=categoriesview)
                new_Computer_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for computer")
                return render(request, 'addpost.html')

        elif(subcategories=='tvvideo'):
            form = Tv_video_sub_category_form(request.POST,request.FILES)
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
                tv_video_sub_categoryview=request.POST.get("tv_video_sub_category", "")
                new_Tv_video_sub_category_object = Tv_video_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,tv_video_sub_category=tv_video_sub_categoryview
                ,categories=categoriesview)
                new_Tv_video_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for tv video")
                return render(request, 'addpost.html')

        elif(subcategories=='camera'):
            form = Camera_sub_category_form(request.POST,request.FILES)
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
                camera_item_sub_categoryview=request.POST.get("camera_item_sub_category", "")
                new_Camera_sub_category_object = Camera_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,camera_item_sub_category=camera_item_sub_categoryview
                ,categories=categoriesview)
                new_Camera_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for camera")
                return render(request, 'addpost.html')

        elif(subcategories=='games'):
            form = Games_sub_category_form(request.POST,request.FILES)
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
                Games_item_sub_categoryview=request.POST.get("Games_item_sub_category", "")
                new_Games_sub_category_object = Games_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,Games_item_sub_category=Games_item_sub_categoryview
                ,categories=categoriesview)
                new_Games_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for games")
                return render(request, 'addpost.html')

        elif(subcategories=='fridge'):
            form = Fridge_ac_washingmachine_form(request.POST,request.FILES)
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
                Fridge_ac_washingmachine_sub_categoryview=request.POST.get("Fridge_ac_washingmachine_sub_category", "")
                new_Fridge_ac_washingmachine_object = Fridge_ac_washingmachine(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,Fridge_ac_washingmachine_sub_category=Fridge_ac_washingmachine_sub_categoryview
                ,categories=categoriesview)
                new_Fridge_ac_washingmachine_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for fridge")
                return render(request, 'addpost.html')
    
        elif(subcategories=='kitchen'):
            form = Kitchen_other_form(request.POST,request.FILES)
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
                Kitchen_other_sub_categoryview=request.POST.get("Kitchen_other_sub_category", "")
                new_Kitchen_other_object = Kitchen_other(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,Kitchen_other_sub_category=Kitchen_other_sub_categoryview
                ,categories=categoriesview)
                new_Kitchen_other_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for kitchen")
                return render(request, 'addpost.html')

        elif(subcategories=='commercial'):
            form = Commercial_vehicle_sub_category_form(request.POST,request.FILES)
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
                kilometers_drivenview = request.POST.get("kilometers_driven", "")
                year_manufactureview = request.POST.get("year_manufacture", "")
                fuelview = request.POST.get("fuel", "")
                commercial_vehicle_brand_nameview=request.POST.get("commercial_vehicle_brand_name", "")
                new_Commercial_vehicle_sub_category_object = Commercial_vehicle_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,commercial_vehicle_brand_name=commercial_vehicle_brand_nameview
                ,kilometers_driven=kilometers_drivenview
                ,year_manufacture=year_manufactureview
                ,fuel=fuelview
                ,categories=categoriesview)
                new_Commercial_vehicle_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for commercial")
                return render(request, 'addpost.html')

        elif(subcategories=='other'):
            form = Other_vehicles_sub_category_form(request.POST,request.FILES)
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
                kilometers_drivenview = request.POST.get("kilometers_driven", "")
                year_manufactureview = request.POST.get("year_manufacture", "")
                fuelview = request.POST.get("fuel", "")
                Other_vehicles_brand_nameview=request.POST.get("Other_vehicles_brand_name", "")
                Other_vehicles_sub_category_object = Other_vehicles_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,Other_vehicles_brand_name=Other_vehicles_brand_nameview
                ,kilometers_driven=kilometers_drivenview
                ,year_manufacture=year_manufactureview
                ,fuel=fuelview
                ,categories=categoriesview)
                Other_vehicles_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for commercial")
                return render(request, 'addpost.html')

        elif(subcategories=='spare_cars'):
            form = Spare_parts_cars_sub_category_form(request.POST,request.FILES)
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
                fuelview = request.POST.get("fuel", "")
                new_Spare_parts_cars_sub_category_object = Spare_parts_cars_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,fuel=fuelview
                ,categories=categoriesview)
                new_Spare_parts_cars_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for spare cars")
                return render(request, 'addpost.html')


        elif(subcategories=='motorcycle'):
            form = Motorcycles_sub_category_form(request.POST,request.FILES)
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
                motorcycle_brand_nameview = request.POST.get("motorcycle_brand_name", "")
                bikes_modelview = request.POST.get("bikes_model", "")
                categoriesview = request.POST.get("categories", "")
                kilometers_drivenview = request.POST.get("kilometers_driven", "")
                year_manufactureview = request.POST.get("year_manufacture", "")
                fuelview = request.POST.get("fuel", "")
                Other_vehicles_brand_nameview=request.POST.get("Other_vehicles_brand_name", "")
                new_Motorcycles_sub_category_object = Motorcycles_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,motorcycle_brand_name=motorcycle_brand_nameview
                ,bikes_model=bikes_modelview
                ,kilometers_driven=kilometers_drivenview
                ,year_manufacture=year_manufactureview
                ,fuel=fuelview
                ,categories=categoriesview)
                new_Motorcycles_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for motorcycle")
                return render(request, 'addpost.html')

        elif(subcategories=='bicycle'):
            form = Bicycles_sub_category_form(request.POST,request.FILES)
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
                bicycle_brand_nameview=request.POST.get("bicycle_brand_name", "")
                new_Bicycles_sub_category_object = Bicycles_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,bicycle_brand_name=bicycle_brand_nameview
                ,categories=categoriesview)
                new_Bicycles_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for bicycle")
                return render(request, 'addpost.html')

        elif(subcategories=='spare_bikes'):
            form = Spare_parts_bikes_sub_category_form(request.POST,request.FILES)
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
                spare_bikes_nameview=request.POST.get("spare_bikes_name", "")
                new_Spare_parts_bikes_sub_category_object = Spare_parts_bikes_sub_category(title=titleview,
                price=priceview,
                photo=request.FILES['photo'],
                subcategories=subcategoriesview,
                description=descriptionview
                ,name=nameview
                ,phone_number=phone_numberview
                ,city=cityview
                ,spare_bikes_name=spare_bikes_nameview
                ,categories=categoriesview)
                new_Spare_parts_bikes_sub_category_object.save()
                return HttpResponseRedirect('/sookh/addpost/')
            else:
                print("form invalid for spare bikes spares")
                return render(request, 'addpost.html')

        elif(subcategories=='furniture'):
            form = Furniture_Form()
            print(form)
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
            form = Furniture_Form(request.POST,request.FILES)
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

def get_ip(request):
    """Returns the IP of the request, accounting for the possibility of being
    behind a proxy.
    """
    ip = request.META.get("HTTP_X_FORWARDED_FOR", None)
    if ip:
        # X_FORWARDED_FOR returns client1, proxy1, proxy2,...
        ip = ip.split(", ")[0]
    else:
        ip = request.META.get("REMOTE_ADDR", "")
    return ip
