from django.shortcuts import render
from appwithmodels.models import Mobiles, Electronics

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
