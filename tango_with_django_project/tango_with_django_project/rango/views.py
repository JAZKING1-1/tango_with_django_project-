from django.http import HttpResponse
from django.shortcuts import render#


def index(request):
    about_link = '<a href="/rango/about/">About page</a>'
    return HttpResponse(f"Rango says hey there partner! Check out the {about_link}.")




def about(request):
    index_link = '<a href="/rango/">Index page</a>'
    return HttpResponse(f"Rango says here is the about page. Go back to the {index_link}.")