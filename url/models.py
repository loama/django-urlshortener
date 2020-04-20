from django.db import models

# Create your models here.

class shortened_url(models.Model):
    original_url = models.CharField(max_length=200)
    shortened_url = models.CharField(max_length=20)

    def __str__(self):
        return self.shortened_url
