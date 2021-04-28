from django.db import models
from django.contrib.auth.models import AbstractUser
from diary.models import Diary, Post
from django.utils.translation import ugettext_lazy as _

class User(AbstractUser):
    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)

    # Constant
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('not-specified', 'Not specified'),
    )

    # 확장하여 추가해줄 필드
    age = models.IntegerField(blank=True, null=True)
    user_id = models.CharField(max_length=20, blank=False, null=True)
    password = models.CharField(max_length=20, blank=False, null=True)
    phone = models.CharField(max_length=140, null=True)
    gender = models.CharField(max_length=80, choices=GENDER_CHOICES, null=True)

    def now_age(self):
        import datetime
        if self.birth_date is None:
            raise ValueError(_('birth_date must be set'))
        return int((datetime.date.today() - self.birth_date).days / 365.25 + 1)

    
class Account(models.Model):
    account_num = models.CharField(max_length=255, blank=False)
    bank = models.CharField(max_length=30, blank=False)
    money = models.PositiveIntegerField(default=0, null=True, blank=False)