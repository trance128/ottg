"""
Standard Django Views
"""

from django.shortcuts import render

def home_page(request):
    """
    Displays the landing page
    """
    return render(request, "home.html")
