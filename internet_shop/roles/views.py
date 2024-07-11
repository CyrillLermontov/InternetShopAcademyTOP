from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema, OpenApiTypes, OpenApiParameter

from base.responses import SuccessGetResponse, BadGetResponse
from .serializer import RolesSerializer
from .models import Roles
from base.BaseViewSet import BaseViewSet
from authentication.dependencies import role_required
from .RolesDAO import RolesDAO


class RolesViewSet(BaseViewSet):
    serializer_class = RolesSerializer
    model = Roles

    @role_required(5, 7)
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @role_required(5, 7)
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @role_required(5, 7)
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @role_required(5, 7)
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    @role_required(5, 7)
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    @role_required(5, 7)
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)

    @role_required(5, 7)
    @extend_schema(
        parameters=[OpenApiParameter('role_name', type=OpenApiTypes.STR,
                                     description='Enter the role name to search for',
                                     required=True)],
        responses={200: RolesSerializer(many=True)}
    )
    @action(detail=False, methods=['get'], url_path='search')
    def search_category(self, request):
        role_name = request.query_params.get('role_name', None)
        if role_name is not None:
            roles = RolesDAO.find_by_name(role_name)
            if not roles:
                return BadGetResponse(data=[])
            serializer = self.serializer_class(roles, many=True)
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])
