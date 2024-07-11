from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView


urlpatterns = [
    path('clients/', include('clients.urls')),
    path('auth/', include('authentication.urls')),
    path('roles/', include('roles.urls')),
    path('products/', include('products.urls')),
    path('categories/', include('categories.urls')),
    path('admin/', admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
]
