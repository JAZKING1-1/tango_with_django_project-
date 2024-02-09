import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def add_page(category, title, url, views=0):
    page = Page.objects.get_or_create(category=category, title=title, url=url, views=views)[0]
    return page

def add_category(name, views=0, likes=0):
    category = Category.objects.get_or_create(name=name, views=views, likes=likes)[0]
    return category

def populate():
    python_cat = add_category('Python', views=128, likes=64)
    add_page(category=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/3/tutorial/",
             views=50)
    add_page(category=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/",
             views=30)
    add_page(category=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/",
             views=20)

    django_cat = add_category("Django", views=64, likes=32)
    add_page(category=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/2.1/intro/tutorial01/",
             views=40)
    add_page(category=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/",
             views=25)
    add_page(category=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/",
             views=35)

    other_cat = add_category("Other Frameworks", views=32, likes=16)
    add_page(category=other_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/",
             views=15)
    add_page(category=other_cat,
             title="Flask",
             url="http://flask.pocoo.org",
             views=20)

    # Print out what we have added to the user
    for cat in Category.objects.all():
        for page in Page.objects.filter(category=cat):
            print(f'- {cat}: {page}')

if __name__ == '__main__':
    print("Starting Rango population script...")
    populate()
