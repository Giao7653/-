from django.urls import path
from . import views

urlpatterns = [
    path('allStem', views.allStem),
    path('todayRecommend', views.todayRecommend),
    path('findStem/<int:stem_id>', views.findStem),
    path('search', views.search),
    path('xYearHot', views.xYearHot),
    path('stemCommentQuery', views.stemCommentQuery),
    path('saveStemComment', views.saveStemComment),
    path('searchTimesHot', views.searchTimesHot),
    path('userSaveStem', views.userSaveStem),
    path('getStemInTime', views.getStemInTime),
    path('categoryComment', views.categoryComment),
]
