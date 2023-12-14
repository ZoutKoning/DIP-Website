from django.contrib import admin
# DO THESE MAYBE GO INTO DIP ADMIN? CHECK LATER
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Account

# Register your models here.
class AccountInline(admin.StackedInline):
    model = Account
    can_delete = False
    verbose_name_plural = "Account"


class UserAdmin(BaseUserAdmin):
    inlines = [AccountInline]


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Account)
