from rest_framework import viewsets
from rest_framework import serializers

from .responses import (
    SuccessGetResponse, BadGetResponse,
    SuccessPostResponse, BadPostResponse,
    SuccessPutResponse, BadPutResponse,
    SuccessDeleteResponse, BadDeleteResponse,
)
from .BaseDAO import BaseDAO
from database import Base
from authentication.dependencies import role_required


class BaseViewSet(viewsets.ModelViewSet):
    serializer_class: serializers.Serializer = serializers.Serializer
    model: Base = Base

    @role_required(5, 6, 7, 8)
    def list(self, request, *args, **kwargs):
        queryset = BaseDAO.find_all(model=self.model)
        serializer = self.serializer_class(queryset, many=True)
        if serializer.data:
            return SuccessGetResponse(data=serializer.data)
        return BadGetResponse(data=[])

    @role_required(5, 6, 7, 8)
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        result = BaseDAO.add(self.model, serializer.data)
        response_serializer = self.get_serializer(result)
        if result is None:
            return BadPostResponse(data=[])
        return SuccessPostResponse(data=response_serializer.data)

    @role_required(5, 6, 7, 8)
    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = BaseDAO.find_by_id(self.model, pk)
        if result is None:
            return BadGetResponse(data=[])
        serializer = self.serializer_class(result[0])
        return SuccessGetResponse(data=serializer.data)

    @role_required(5, 6, 7, 8)
    def update(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = BaseDAO.find_by_id(self.model, pk)
        if result is None:
            return BadPutResponse(data=[])
        result = BaseDAO.update(self.model, pk, request.data)
        serializer = self.serializer_class(result)
        return SuccessPutResponse(data=serializer.data)

    @role_required(5, 6, 7, 8)
    def partial_update(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    @role_required(5, 6, 7, 8)
    def destroy(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        result = BaseDAO.find_by_id(self.model, pk)
        if result is None:
            return BadDeleteResponse(data=[])
        BaseDAO.delete(self.model, pk)
        serializer = self.serializer_class(result)
        return SuccessDeleteResponse(data=serializer.data)