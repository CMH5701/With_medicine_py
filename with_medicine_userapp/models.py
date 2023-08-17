from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth import get_user_model

# Create your models here. 

class CustomUser(AbstractUser):
    name = models.CharField(max_length=10, null = True, blank=True)
    age = models.IntegerField(null = True, blank=True)
    email = models.CharField(max_length=50, null = True, blank=True)
    image = models.ImageField(blank=True)
    genders = {
        ('M', '남성(Man)'), 
        ('W', '여성(Woman)'), 
        ('O', '기타(Other)'),
    }
    gender = models.CharField(verbose_name='성별', max_length=1, choices=genders , null = True, blank=True)
    phone_number = models.CharField(max_length=50, null = True, blank=True)
    
class HealthInfo(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='health_info')
    height = models.DecimalField(max_digits=5, decimal_places=2) # 소수점 2자리
    weight = models.DecimalField(max_digits=5, decimal_places=2) 
    medical_history = models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username