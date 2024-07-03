from django.contrib import admin

from users.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'is_staff')
    list_filter = ('is_staff',)
    search_fields = ('email',)
