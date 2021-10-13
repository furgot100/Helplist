from django.urls import path
from list.views import HelperListView, HelperCreateView, HelperDetailView



urlpatterns = [
    path('', HelperListView.as_view(), name='listing-page'),
    path('new/', HelperCreateView.as_view(), name='helper-new-page'),
    path('<str:slug>/', HelperDetailView.as_view(), name='helper-detail'),

]