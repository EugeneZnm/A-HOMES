from django.shortcuts import render, get_object_or_404
from .choices import price_choices, bedroom_choices, county_choices
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

# Create your views here.
def index(request):

    # getting published listings by order of date in descending order
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    context = {
        'listings':pages
    }

    return render (request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing,
        
    }

    return render (request, 'listings/listing.html',context)   

def search(request):

    queryset_list = Listing.objects.order_by('-list_date')

    # keywords
    if 'keywords' in request.GET:
     keywords = request.GET['keywords']
     if keywords:
            queryset_list = queryset_list.filter(description__icontains=keywords)

    # City

    if 'city' in request.GET:
        cities = request.GET['city']
        if cities:
            queryset_list = queryset_list.filter(city__iexact=cities)

    # County
    if 'county' in request.GET:
        county = request.GET['county']
        if county:
            queryset_list = queryset_list.filter(county__iexact=county) 

     # Bedrooms
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset_list = queryset_list.filter(bedrooms__lte=bedrooms)         

     # pricing
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset_list = queryset_list.filter(price__lte=price)                 


    paginator = Paginator(queryset_list,3)
    page = request.GET.get('page')
    pages = paginator.get_page(page)

    context ={
        'county_choices': county_choices,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': pages,

        # store search term in field after result delivery
        'values':request.GET
    }
    return render (request, 'listings/search.html', context)