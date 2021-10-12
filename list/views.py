from django.http import HttpResponse


# from list.models import Listing


def index(request):
    return HttpResponse("Hello, world")