from django.db import models

# Create your models here.
class farmer(models.Model):
    e_name=models.CharField(max_length=30)
    e_age= models.CharField(max_length=2)
    e_phone=models.CharField(max_length=10)
    e_desc=models.TextField()

    def __str__(self):
        return self.e_name