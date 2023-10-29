from django.db import models

# Create your models here.


class Items(models.Model):
  title  = models.CharField(max_length=100, null=True, blank=True)
  image = models.CharField(max_length=100, null=True, blank=True)
  likes = models.PositiveIntegerField(default=0)
  
  
  def __str__(self):
    return f"{self.title}"
  
  

class User(models.Model):
  pass