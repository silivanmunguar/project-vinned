from django.db import models

# Create your models here.
class users(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    User_email = models.EmailField(max_length = 254)
    