from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model  # settings.AUTH_USER_MODEL랑 같은 의미

# Create your models here.
class Free_board(models.Model):
    title = models.CharField(max_length=100)
    pub_date = models.DateTimeField('data published')
    body = models.TextField()
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, default=1, related_name="l_posts")
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_posts', blank=True)
    hits = models.IntegerField(default=0)
    image = models.ImageField(blank=True)
    def __str__(self):
        return self.title

class Free_Comment(models.Model):
    free_board_id = models.ForeignKey(Free_board, on_delete=models.CASCADE, related_name='comment')
    b_text = models.CharField(max_length=30)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, default=1, related_name="l_posts_comment")
    image = models.ImageField(blank=True)
    
    def __str__(self):
        return self.b_text 