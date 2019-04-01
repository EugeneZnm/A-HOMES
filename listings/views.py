from django.shortcuts import render, get_object_or_404
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
        'listing': listing
    }

    return render (request, 'listings/listing.html',context)   

def search(request):
    return render (request, 'listings/search.html')