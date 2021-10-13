from typing import List
from django.http import HttpResponse, Http404
from django.views.generic.list import ListView
from django.shortcuts import render
from list.models import Listing
from django.views.generic.edit import CreateView
from list.forms import ListCreateForm
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView


class HelperListView(ListView):
    """ Renders a list of all Pages. """
    model = Listing

    def get(self, request):
        """ GET a list of Pages. """
        lists = self.get_queryset().all()
        return render(request, 'list.html', {
          'lists': lists
        })

class HelperCreateView(CreateView):
    def get(self, request, *args, **kwargs):
        product = {'form': ListCreateForm()}
        return render(request, 'new.html', product)

    def post(self, request, *args, **kwargs):
        form = ListCreateForm(request.POST)
        if form.is_valid():
            item = form.save()
            item.save()
            return HttpResponseRedirect(reverse_lazy('list:listing-page'))
        return render(request,'new.html', {'form': form})

# class HelperDetailView(DetailView):
#     """ Renders a specific page based on it's slug."""
#     model = Listing

#     def get(self, request, slug):
#         try:
#             list = Listing.objects.get(slug=slug)
#         except Listing.DoesNotExist:
#             raise Http404("Product doesn't exist")
#         return render(request, 'detail.html', {'list' : list})