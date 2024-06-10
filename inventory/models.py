from django.template.defaultfilters import slugify
from django.utils import timezone

from django.db import models
# unique slugify generator
def unique_slugify(instance, slug):
        model = instance.__class__
        unique_slug = slug
        record_count = 0
        while model.objects.filter(slug=unique_slug).exists():
            unique_slug = slug + "-1"
            while model.objects.filter(slug=unique_slug).exists():
                record_count = record_count + 1
                unique_slug = slug + "-" + str(record_count)
        return unique_slug

class Supplier(models.Model):
    slug = models.SlugField(max_length=100, 
                            null=False, blank=False, 
                            editable=False, 
                            allow_unicode=True) 
    name = models.CharField(max_length=100,null=True,blank=True)
    contact_info = models.TextField(null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True,blank=True)
    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.name)
            self.slug = unique_slugify(self, slug_text)
        super().save(*args, **kwargs)

    def soft_delete(self):
        self.date_deleted = timezone.now()
        self.save()

class InventoryItem(models.Model):
    slug = models.SlugField(max_length=100, 
                            null=False, blank=False, 
                            editable=False, 
                            allow_unicode=True) 
    name = models.CharField(max_length=100,null=True,blank=True)
    description = models.TextField(null=True,blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null=True,blank=True)
    suppliers = models.ManyToManyField(Supplier, related_name='items')
    date_added = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_deleted = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        if not self.slug:
            slug_text = slugify(self.name)
            self.slug = unique_slugify(self, slug_text)
        super().save(*args, **kwargs)
    def soft_delete(self):
        self.date_deleted = timezone.now()
        self.save()