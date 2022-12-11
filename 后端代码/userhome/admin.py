from django.contrib import admin

from userhome.models import User


class UserManager(admin.ModelAdmin):
    list_display = ['username', 'is_active', 'create_time']
    list_display_links = ['username']  # 超链接
    search_fields = ['username']  # 添加搜索框(模糊)


admin.site.register(User, UserManager)
