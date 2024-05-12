from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import status, generics
from apps.products.models import Product
from rest_framework.response import Response

from django.utils import timezone
from .models import Order, OrderItem

# import timez

# Create your views here.


class AddToCart(APIView):
    """
    This is responsible for the add to cart functionality.
    This first gets the user to
    """

    def post(self, request, id):

        # check whether product exists
        print(id)

        product = Product.objects.get(id=id)

        print(product)

        order_item, created = OrderItem.objects.get_or_create(
            item=product, buyer=request.user
        )

        print(order_item, created)

        order_qs = Order.objects.filter(buyer=request.user, ordered=False)

        if order_qs:
            order = order_qs[0]

            if order.orderItems.filter(order_item__id=id).exists():
                order_item.quantity += 1
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
