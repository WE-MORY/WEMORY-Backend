
from django.db import models
#from user.models import User, Account


class Diary(models.Model):
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
#    account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
    title = models.CharField(max_length=50)
    goal = models.PositiveIntegerField(default=0, null=True,)

    
class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True)
    image = models.ImageField(blank=True, null=True, upload_to="Post/%Y/%m/")
#    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    diary = models.ForeignKey(Diary, blank=False, null=False, on_delete=models.CASCADE)
