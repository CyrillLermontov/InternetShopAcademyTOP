from base.responses import SuccessGetResponse, BadGetResponse
from .serializer import OrderHistorySerializer
from .models import OrderHistory
from .OrderHistoryDAO import OrderHistoryDAO
from authentication.dependencies import role_required
from base.BaseViewSet import BaseViewSet


class OrderHistoryViewSet(BaseViewSet):
    serializer_class = OrderHistorySerializer
    model = OrderHistory

    @role_required(5, 6, 7, 8)
    def list(self, request, *args, **kwargs):
        orders = OrderHistoryDAO.find_all_orders()
        serializer = self.serializer_class(orders, many=True)
        return SuccessGetResponse(data=serializer.data)
    
    @role_required(5, 6, 7, 8)
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = OrderHistoryDAO.find_order_by_id(pk)
        if result is None:
            return BadGetResponse(data=[])
        serializer = self.serializer_class(result[0])
        return SuccessGetResponse(data=serializer.data)

    @role_required(5, 7)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    @role_required(5, 7)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @role_required(5, 7)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

