from django.contrib import admin
from django.urls import path, include

from util import views as util_views
from lionapp import views as lion_views
from member import views as member_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('util.urls')), 
    path('lion/', include('lionapp.urls')),
    path('member/', include('member.urls')),
    path('users/', include('users.urls')),
    path('', util_views.home, name='home'),  # 기본 경로 추가
]