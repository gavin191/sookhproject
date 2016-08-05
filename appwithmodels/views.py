from django.shortcuts import render, 
from django.views.decorators.csrf import csrf_protect 
from appwithmodels.models import Mobiles, Electronics
from appwithmodels impost forms as frms

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        selector = request.POST.get("selector", "")
        if(selector=="Cars_sub_category"):
            form = frms.Cars_sub_category(request.POST)
            if form.is_valid():
                return HttpResponseRedirect()
            else:
                return render(request, 'addpost.html')

