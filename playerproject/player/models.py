from django.db import models

# Create your models here.
class PlayersDetails(models.Model):
    name=models.TextField(max_length=100)
    test_innings=models.IntegerField()
    runs=models.IntegerField()
