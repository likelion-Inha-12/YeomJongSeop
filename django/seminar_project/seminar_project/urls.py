from django.contrib import admin
from django.urls import path, include, re_path

from util import views as util_views
from lionapp import views as lion_views
from member import views as member_views
# urls.py
from django.conf import settings
from django.conf.urls.static import static

from rest_framework.permissions import AllowAny
from drf_yasg.views import get_schema_view
from drf_yasg       import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="프로젝트 이름(예: likelion-project)",
        default_version='프로젝트 버전(예: 1.1.1)',
        description="해당 문서 설명(예: likelion-project API 문서)",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="likelion@inha.edu"), # 부가정보
        license=openapi.License(name="backend"),     # 부가정보
    ),
    public=True,
    permission_classes=(AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('health/', include('util.urls')), 
    path('lion/', include('lionapp.urls')),
    path('member/', include('member.urls')),
    path('users/', include('users.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #path('', views.index, name='index'),
    #path('', util_views.home, name='home'),  # 기본 경로 추가
    # Swagger url
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)