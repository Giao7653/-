from django.contrib import admin
from .models import Stem, StemComment, StemRecommend, StemImage, StemSearchTimes


class StemManager(admin.ModelAdmin):
    list_display = ['stem', 'create_time']
    list_display_links = ['stem']  # 超链接
    list_filter = ['year']  # 右侧过滤器
    search_fields = ['stem']  # 添加搜索框(模糊)


class StemCommentManager(admin.ModelAdmin):
    list_display = ['stem_id', 'content', 'username', 'create_time']
    list_display_links = ['stem_id']  # 超链接
    search_fields = ['stem_id']  # 添加搜索框(模糊)


class StemRecommendManager(admin.ModelAdmin):
    list_display = ['today', 'stem_id', 'stem', 'create_time']
    list_display_links = ['today']  # 超链接
    list_filter = ['today']  # 右侧过滤器
    search_fields = ['today']  # 添加搜索框(模糊)


class StemImageManager(admin.ModelAdmin):
    list_display = ['stem_image', 'stem_id', 'create_time']
    list_display_links = ['stem_id']  # 超链接
    search_fields = ['stem_image']  # 添加搜索框(模糊)


class StemSearchTimesManager(admin.ModelAdmin):
    list_display = ['search_content', 'search_times', 'create_time']
    list_display_links = ['search_content']  # 超链接
    search_fields = ['search_content']  # 添加搜索框(模糊)


admin.site.register(StemImage, StemImageManager)
admin.site.register(StemRecommend, StemRecommendManager)
admin.site.register(Stem, StemManager)
admin.site.register(StemComment, StemCommentManager)
admin.site.register(StemSearchTimes, StemSearchTimesManager)