from django.db import models
from diary.models import Diary

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, blank=True)
    diary = models.ForeignKey("diary.Diary", related_name="post_list", blank=False, null=False, on_delete=models.CASCADE)
