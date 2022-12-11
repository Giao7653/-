from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login),
    path('register', views.register),
    path('login_out', views.login_out),
    path('sendEmailCode', views.sendEmailCode),
    path('getCaptcha', views.getCaptcha),


]
