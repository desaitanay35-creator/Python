from django.db import models

# Create your models here.
class Players (models.Model):
    name= models.CharField(max_length=100)
    runs= models.IntegerField()
    profile=models.URLField(max_length=200)
    email=models.EmailField(max_length=254)
    bod = models.DateField(blank=True)

    def __str__(self):
        return self.name