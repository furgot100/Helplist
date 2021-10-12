from django.urls import path
from list.views import PageListView

from . import views

urlpatterns = [
    path('', PageListView.as_view(), name='listing-page'),
]