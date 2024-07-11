from django.urls import path, include

from .router import router as categories_router

urlpatterns = [
    path('', include(categories_router.urls)),
]
