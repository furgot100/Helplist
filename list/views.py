from django.http import HttpResponse
from django.views.generic.list import ListView
from django.shortcuts import render
from list.models import Listing


class PageListView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request):
        """ GET a list of Pages. """
        lists = self.get_queryset().all()
        return render(request, 'list.html', {
          'lists': lists
        })