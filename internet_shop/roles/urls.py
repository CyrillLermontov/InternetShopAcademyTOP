from django.urls import path, include

from .router import router as roles_router

urlpatterns = [
    path('', include(roles_router.urls)),
]
