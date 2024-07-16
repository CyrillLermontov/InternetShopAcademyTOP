from django.urls import path, include

from .router import router as order_history_router

urlpatterns = [
    path('', include(order_history_router.urls)),
]
