from django.contrib import admin
from .models import *
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
# Register your models here.


class BalanceInline(admin.StackedInline):
    model = Balance
    can_delete = False

# Define a new User admin


class UserAdmin(BaseUserAdmin):
    inlines = (BalanceInline,)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Bet)
admin.site.register(Type)

