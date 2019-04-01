from django.shortcuts import render
from .models import Listing
from django.core.paginator import EmptyPage, Paginator, PageNotAnInteger

# Create your views here.
def index(request):

    # getting listings by order of date in descending order
    listings = Listing.objects.order_by('-list_date')
    paginator = Paginator(listings,3)
    page = request.GET.get('page')
    pages = paginator.get_page(page)
    context = {
        'listings':pages
    }

    return render (request, 'listings/listings.html', context)

def listing(request, listing_id):
    return render (request, 'listings/listing.html')   

def search(request):
    return render (request, 'listings/search.html')