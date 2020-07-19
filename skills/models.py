from django.db import models
from django.urls import reverse

# Create your models here.

class Skills(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=120)
    description = models.TextField()
    img = models.ImageField(default='default.jpg', upload_to='skills_images')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('skill-detail', kwargs={'slug': self.slug})