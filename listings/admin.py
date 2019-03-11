from django.contrib import admin
from .models import Listing

#adding listing object properties that are visible on admin dashboard after publishing
class ListingAdmin(admin.ModelAdmin):
 list_display = ('id', 'title', 'is_published', 'price', 'list_date', 'realtor')

# adding listings model to admin section
admin.site.register(Listing, ListingAdmin)