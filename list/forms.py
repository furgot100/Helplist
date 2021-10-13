from django import forms
from list.models import Listing


class ListCreateForm(forms.ModelForm):
    """ Render and process a form based on the Page model. """
    class Meta:
        model = Listing
        fields = '__all__'