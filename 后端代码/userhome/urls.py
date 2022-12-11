from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('getUserInfo', views.getUserInfo),
    path('updateAvatar', views.updateAvatar),
    path('updateUserinfo', views.updateUserinfo),
    path('authenticationToken', views.authenticationToken),
    path('queryMyStem', views.queryMyStem)

]
