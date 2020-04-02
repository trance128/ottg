"""
Standard Django Views
"""

from django.http import HttpResponse

def home_page(request):
    """
    Displays the landing page
    """
    return HttpResponse('<html><title>To-Do lists</title></html>')
