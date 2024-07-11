from django.urls import path, include

from .router import router as products_router

urlpatterns = [
    path('', include(products_router.urls)),
]
