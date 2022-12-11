from django.urls import path
from . import views

urlpatterns = [
    path('allStemPage', views.allStemPage),
    path('xYearStemPage', views.xYearStemPage),
    path('getStemInTime', views.getStemInTime),

]
