"""
Standard Django Views
"""
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Item

def home_page(request):
    """
    Displays the landing page
    """
    if request.method == "POST":
        Item.objects.create(text=request.POST['item_text'])
        return redirect('/')

    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})
