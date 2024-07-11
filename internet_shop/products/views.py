from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter


from base.responses import SuccessGetResponse, BadGetResponse
from .models import Products
from .serializer import ProductsSerializer
from .ProductsDAO import ProductsDAO
from base.BaseViewSet import BaseViewSet
from authentication.dependencies import role_required


class ProductsViewSet(BaseViewSet):
    serializer_class = ProductsSerializer
    model = Products

    @role_required(5, 7)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @role_required(5, 7)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @role_required(5, 7)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @role_required(5, 7)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @role_required(5, 6, 7, 8)
    @extend_schema(
        parameters=[OpenApiParameter('product_name', type=OpenApiTypes.STR,
                                     description='Enter the product name to search for',
                                     required=True)],
        responses={200: serializer_class(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_product(self, request):
        product_name = request.query_params.get('product_name', None)
        if product_name is not None:
            products = ProductsDAO.find_by_name(product_name)
            if not products:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(products, many=True)
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])