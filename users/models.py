from django.db import models
from django.contrib.auth.models import User


class Auther(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    
    class Meta:
        db_table = "user_auther"
        verbose_name = "auther"
        verbose_name_plural = "authers"
        ordering = ["-id"]
        
    def __str__(self):
          return self.user.username