from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from django.contrib.auth import logout
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from apps.users import permissions as custom_permissions
from config.api import api

schema_view = get_schema_view(
    openapi.Info(
        title="Great API",
        default_version='v1',
        description="Great description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="beatuminflow@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.IsAuthenticatedOrReadOnly, custom_permissions.IsOwnerOrReadOnly),
)

urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    url(r'^api/', include(api.urls)),
    # url(r'^api/auth-user/', include('djoser.urls')),
    url(r'^api/auth-token/', include('djoser.urls.authtoken')),
    url(r'^admin/', admin.site.urls),
    url(r'^logout/', logout, {'next_page': '/'}, name='logout'),
]
#
#
# urlpatterns = [
#     url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
#     url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
#     url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
#     path('api/v1/', include(api.urls)),
#     url(r'^api/v1/auth-user/', include('djoser.urls')),
#     url(r'^api/v1/auth-token/', include('djoser.urls.authtoken')),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
#     path('admin/', admin.site.urls, name='admin'),
#     path('logout/', logout, {'next_page': '/'}, name='logout'),
# ]
