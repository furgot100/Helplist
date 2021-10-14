from django.contrib import admin

from .models import Listing

class ListingAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('title', 'slug', 'author', 'created', 'email')

admin.site.register(Listing)


