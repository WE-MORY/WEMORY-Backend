from django.db import models

# Create your models here.
class Account(models.Model):
    account_num = models.CharField(max_length=255, blank=False)
    bank = models.CharField(max_length=30, blank=False)
    money = models.PositiveIntegerField(default=0, null=True, blank=False)
    user = models.ForeignKey("user.User", on_delete=models.CASCADE, blank=True)
