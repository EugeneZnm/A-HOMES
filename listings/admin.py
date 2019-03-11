from django.contrib import admin
from .models import Listing

# adding listings model to admin section
admin.site.register(Listing)