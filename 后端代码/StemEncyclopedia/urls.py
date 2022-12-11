from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.views.static import serve
from django.views import static
from StemEncyclopedia import views

urlpatterns = [
    # path('', views.sites),
    path('admin/', admin.site.urls),
    path('authorization/', include('authorization.urls')),
    path('stem/', include('stem.urls')),
    path('userhome/', include("userhome.urls")),
    path('page/', include('page.urls')),
    path('captcha/', include('captcha.urls')),  # 图片验证码
    url(r'^static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),

]
