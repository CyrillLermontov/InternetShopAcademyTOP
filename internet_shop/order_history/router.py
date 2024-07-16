from rest_framework import routers

from .views import *


router = routers.DefaultRouter()


router.register(r'', OrderHistoryViewSet, basename="order-history")