"""
Standard Django Views
"""
from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    """
    Displays the landing page
    """
    return render(request, 'home.html', {
        'new_item_text': request.POST.get('item_text', ''),
    })
