from django.conf import settings
from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils import timezone
from django.contrib.auth.models import User

class Listing(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    slug = models.CharField(max_length=settings.POST_TITLE_MAX_LENGTH, blank=True, editable=False,
                            help_text="Unique URL path to access this page. Generated by the system.")

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.pk:
            self.slug = slugify(self.title, allow_unicode=True)
        return super(Listing, self).save(*args, **kwargs)

    def get_absolute_url(self):
        """ Returns a fully-qualified path for a page"""
        path_components = {'slug': self.slug}
        return reverse('store-item', kwargs=path_components)    
