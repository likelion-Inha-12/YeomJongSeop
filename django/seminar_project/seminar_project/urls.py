from django.contrib import admin
from django.urls import path, include

from util import views
from lionapp import views
from member import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('util.urls')), 
    path('lion/', include('lionapp.urls')),
    path('member/', include('member.urls')),
]