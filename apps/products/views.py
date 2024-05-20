from django.shortcuts import render


import django_filters
import logging

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import filters, generics, permissions, status

from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.views import APIView

from .exceptions import ProductNotFound, CategoryNotFound
from .serializers import ProductSerializer, CategorySerializer
from .models import Product, Category
from .pagination import ProductPagination


logger = logging.getLogger(__name__)


class ProductFilter(django_filters.FilterSet):
    price = django_filters.NumberFilter()
    price__gt = django_filters.NumberFilter(field_name="price", lookup_expr="gt")
    price__lt = django_filters.NumberFilter(field_name="price", lookup_expr="lt")

    class Meta:
        model = Product
        fields = [
            "price",
        ]


class ListAllProductAPIView(generics.ListAPIView):
    #  this allows for even unathenticated users to browse the products
    serializer_class = ProductSerializer
    queryset = Product.selling.all().order_by("-created_at")
    pagination_class = ProductPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_class = ProductFilter
    search_fields = ["name"]
    ordering_fields = ["created_at"]


class GetProductDetail(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, id):
        product = Product.objects.get(id=id)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)


class CreateProductApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        data = request.data
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": "created"}, status=status.HTTP_201_CREATED)
        return Response({"error": "Not created"}, status=status.HTTP_400_BAD_REQUEST)
