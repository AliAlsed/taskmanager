from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class News(models.Model):
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    short_description = models.CharField(max_length=100)
    Author = models.CharField(max_length=100)
    Image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return self.title
