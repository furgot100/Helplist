from django import forms
from list.models import Listing


class ListCreateForm(forms.ModelForm):
    class Meta:
        model = Listing
        fields = '__all__'