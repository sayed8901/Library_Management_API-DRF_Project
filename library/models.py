from accounts.models import CustomUser
from django.db import models
from django.utils.text import slugify


# Create your models here.

# category model
class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100, blank=True, null=True, unique=True)

    # to add automatically slug values after a category is created or its name updated
    def save(self, *args, **kwargs):
        # Check if this is a new object by checking if self.pk is None
        if not self.pk:  
            # It's a new object, so create a new slug
            self.slug = slugify(self.name)
        else:
            # Object already exists, check if the name has changed to update the slug
            existing = Category.objects.get(pk=self.pk)
            if existing.name != self.name:
                self.slug = slugify(self.name)

            self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


    def __str__(self):
        return f'{self.name}'


# book model
class Book(models.Model):
    title = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='books')
    author = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    quantity = models.PositiveIntegerField()
