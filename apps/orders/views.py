from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import filters, status, generics, permissions
from apps.products.models import Product
from rest_framework.response import Response

from django.utils import timezone
from .models import Order, OrderItem
from .serializer import OrderSerializer
from django.db import transaction, DatabaseError
import django_filters

from django_filters.rest_framework import DjangoFilterBackend


# from .producer import publish

# Create your views here.


class OrderFilter(django_filters.FilterSet):
    ordered = django_filters.BooleanFilter()

    class Meta:
        model = Order
        fields = ["ordered"]


class GetAllOrders(generics.ListAPIView):

    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]

    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]

    filterset_class = OrderFilter

    search_fields = ["ordered"]

    def get_queryset(self):
        # publish()
        return Order.objects.filter(buyer=self.request.user)


class AddToCart(APIView):
    """
    This is responsible for the add to cart functionality.
    This first gets the user to
    """

    def post(self, request, id):

        product = Product.objects.get(id=id)

        # raise error when product is not being sold here

        if product.is_selling is False:
            return Response(
                {"data": "The product selected is not for sale"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        order_item, created = OrderItem.objects.get_or_create(
            item=product, buyer=request.user
        )

        order_qs = Order.objects.filter(buyer=request.user, ordered=False)

        try:

            with transaction.atomic():

                if order_qs:
                    order = order_qs[0]

                    if order.orderItems.filter(item__id=id).exists():
                        order_item.quantity += 1
                        product.quantity -= 1
                        product.save()
                        order_item.save()
                    else:
                        order.orderItems.add(order_item)

                else:
                    order = Order.objects.create(
                        buyer=request.user, ordered_date=timezone.now()
                    )
                    order.orderItems.add(order_item)
                    order.save()

                return Response({"data": "done"}, status=status.HTTP_200_OK)
        except DatabaseError as error:
            print(error)
            return Response(
                {"data": "An error occured"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


class RemoveFromCart(APIView):
    """
    This handles the remove from cart functionality"""

    def patch(self, request, id):

        product = Product.objects.get(id=id)

        # raise error when product is not being sold here

        # if product.is_selling is False:
        #     return Response(
        #         {"data": "The product selected is not for sale"},
        #         status=status.HTTP_400_BAD_REQUEST,
        #     )

        order_item = OrderItem.objects.get(
            item=product, ordered=False, buyer=request.user
        )

        order_qs = Order.objects.filter(ordered=False, buyer=request.user)

        if order_qs:
            order = order_qs[0]
            if order.orderItems.filter(item__id=id).exists():
                order.orderItems.remove(order_item)
                # delete the order items

                # return the item number to the product
                product.quantity += order_item.quantity
                order_item.delete()
                product.save()
            return Response(
                {"data": "Removed from cart success"}, status=status.HTTP_200_OK
            )

        return Response(
            {"data": "Item not found in cart "}, status=status.HTTP_400_BAD_REQUEST
        )


class payCart(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def patch(self, request, id):
        order = Order.objects.get(id=id)

        # publish("pay_order", order)

        return Response({"data": "Order to be processed!!"}, status=status.HTTP_200_OK)
