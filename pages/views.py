from django.shortcuts import render
from django.http import HttpResponse

from listings.models import Listing
from realtors.models import Realtor
from listings.choices import price_choices, bedroom_choices, county_choices
# Create your views here.
def index(request):
    # getting three published listings by date
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)[:3]

    context = {
        'listings':listings,
        'county_choices': county_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
    }

    return render(request, 'pages/index.html', context)

def about(request):

    # Get all Realtors
    realtor = Realtor.objects.order_by('hire_date')

    # GEt mvp realtor
    mvp = Realtor.objects.all().filter(is_mvp=True)

    context = {
        'realtor': realtor,
        'mvp': mvp
    }
    return render(request, 'pages/about.html', context) 