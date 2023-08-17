from django.db import models

# Create your models here.

class Item(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()  # 긴 텍스트 데이터 저장, 텍스트 길이에 제한이 없음
    
    def __str__(self):
        return self.title