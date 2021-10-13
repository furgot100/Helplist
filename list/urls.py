from django.urls import path
from list.views import HelperListView, HelperCreateView

app_name = 'list'

urlpatterns = [
    path('', HelperListView.as_view(), name='listing-page'),

    path('new/', HelperCreateView.as_view(), name='helper-new-page'),
]