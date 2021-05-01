from django.db import models

class Diary(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, blank=True)
    account_num = models.CharField(max_length=255, blank=False)
    bank = models.CharField(max_length=30, blank=False)
    money = models.PositiveIntegerField(default=2000000, null=True, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
    title = models.CharField(max_length=50)
    goal = models.PositiveIntegerField(default=0, null=True)

    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
    author = models.ForeignKey("user.User", on_delete=models.CASCADE, blank=True)
    diary = models.ForeignKey("diary.Diary", blank=False, null=False, on_delete=models.CASCADE)
