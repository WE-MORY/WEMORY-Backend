from django.db import models
#from post.models import Post

class Diary(models.Model):
    id = models.AutoField(primary_key=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    user = models.ForeignKey("user.User", related_name="diary_list", on_delete=models.CASCADE, blank=True)
#    post = models.ForeignKey("post.Post", on_delete=models.CASCADE, blank=True)
    account_num = models.CharField(max_length=255, blank=False)
    bank = models.CharField(max_length=30, blank=False)
    money = models.PositiveIntegerField(default=2000000, null=True, blank=False)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
    title = models.CharField(max_length=50)
    goal = models.PositiveIntegerField(default=0, null=True)

