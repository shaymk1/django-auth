from django.db import models
from django.contrib.auth.models import  AbstractUser



class User(AbstractUser):
  first_name = models.CharField(max_length=255)
  last_name = models.CharField(max_length=255)
  email = models.EmailField(unique=True)
  password = models.CharField(max_length=20)
  username = None

  

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = []

  def __str__(self):
      return self.first_name
    
