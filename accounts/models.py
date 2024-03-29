from django.db import models
from django.contrib.auth.models import User
from PIL import Image
# Create your models here.
class Account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=f'accounts/dp', blank=True)

