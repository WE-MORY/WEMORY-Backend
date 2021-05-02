from django.contrib import admin
from user.models import User
from account.models import Account
# Register your models here.

admin.site.register(User)
admin.site.register(Account)