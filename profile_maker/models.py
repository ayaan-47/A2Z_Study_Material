from django.db import models
from django.urls import reverse
    

# Create your models here.
class mypeople(models.Model):
    name = models.CharField(max_length=200)
    files = models.FileField()
    pmage = models.ImageField(blank = True)
    description = models.TextField()

    def __str__(self):
        return self.name


class ytvideos(models.Model):
    yname = models.CharField(max_length=200)
    ydesc = models.TextField()
    ylink = models.URLField()
    ytmage = models.ImageField(blank = True)

    def __str__(self):
        return self.yname
    def get_absolute_url(self):
        return reverse('realhome')
