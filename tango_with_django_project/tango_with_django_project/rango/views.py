from rango.models import Category
from django.http import HttpResponse
from django.shortcuts import render
from rango.models import Page
from .models import Page

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    context_dict['categories'] = category_list
    top_five_pages = Page.objects.order_by('-views')[:5]

    context_dict['pages'] = top_five_pages
    return render(request, 'rango/index.html', context=context_dict)




def about(request):
    index_link = '<a href="/rango/">Index page</a>'
    context_dict = {}
    #return HttpResponse(f"Rango says here is the about page. Go back to the {index_link}.")
    return render(request, 'rango/about.html', context=context_dict)


def show_category(request, category_name_slug):
    context_dict = {}
    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category
    except Category.DoesNotExist:
        context_dict['pages'] = None
        context_dict['category'] = None
    return render(request, 'rango/category.html', context=context_dict)

