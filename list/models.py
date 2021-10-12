from django.db import models
from django.utils import timezone

class Listing(models.Model):
    title = models.CharField(max_length=120)
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    summary = models.TextField()
    created = models.DateTimeField(auto_now_add=True,
                                   help_text="The date and time this page was created. Automatically generated when the model saves.")
    # author = models.ForeignKey(User, on_delete=models.PROTECT)
    # slug = models.CharField(max_length=settings.POST_TITLE_MAX_LENGTH, blank=True, editable=False)

    def __str__(self):
        return self.title

    # def save(self, *args, **kwargs):
    #     if not self.pk:
    #         self.slug = slugify(self.title, allow_unicode=True)
    #     return super(Products, self).save(*args, **kwargs)

    # def get_absolute_url(self):
    #     """ Returns a fully-qualified path for a page"""
    #     path_components = {'slug': self.slug}
    #     return reverse('store-item', kwargs=path_components)    
