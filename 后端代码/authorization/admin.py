from django.contrib import admin

# from authorization.models import EmailCodeSession

admin.site.site_header = '梗百科管理后台'
admin.site.site_title = '梗百科管理后台'

#
# class EmailCodeSessionManager(admin.ModelAdmin):
#     list_display = ['username', 'code', 'create_time']
#     list_display_links = ['username']  # 超链接
#     search_fields = ['username']  # 添加搜索框(模糊)
#
#
# admin.site.register(EmailCodeSession, EmailCodeSessionManager)
