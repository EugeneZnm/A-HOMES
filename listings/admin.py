from django.contrib import admin
from .models import Listing

#adding listing object properties that are visible on admin dashboard after publishing
class ListingAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')
 list_display_links = ('id', 'title')
 list_filter = ('realtor', 'price')
 list_editable = ('price', 'is_published')
 search_fields = ('title', 'description', 'address', 'city', 'state', 'price')
 list_per_page = 25
 

# adding listings model to admin section
admin.site.register(Listing, ListingAdmin)