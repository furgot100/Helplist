from django.db import models

class Listings(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # price = models.DecimalField(decimal_places=2, max_digits=10000)
    summary = models.TextField()
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
