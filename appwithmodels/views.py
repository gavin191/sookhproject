from django.shortcuts import render
from 
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

def addpost(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = Cars_sub_category(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect()

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
