from django.shortcuts import render, redirect
from .models import Listing
from .forms import ListingForm
# CRUD: CREATE, RETRIEVE, UPDATE, DELETE, LIST

# Create your views here.
def Items(request):
    items = Listing.objects.all()
    context = {
        "items": items
    }
    return render(request, "items.html", context)

def getItem(request, pk):
    item = Listing.objects.get(id=pk)
    context = {
        "item" : item
    } 
    return render(request, "getItem.html", context)

def createItem(request):
    form = ListingForm()
    if request.method == 'POST':
        form = ListingForm(request.POST, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {
        "form" : form
    }
    return render(request, "createItem.html", context)

def updateItem(request, pk):
    item = Listing.objects.get(id=pk)
    form = ListingForm(instance=listing)
    if request.method == 'POST':
        form = ListingForm(request.POST, instance=listing, files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/")
    
    context = {
        "form" : form
    }
    return render(request, "updateItem.html", context)


def deleteItem(request, pk):
    item = Listing.objects.delete(id=pk)
    item.delete()
    redirect("/")
