from . import views
from django.urls import path

urlpatterns = [
    path("", views.GetAllOrders.as_view(), name="get_all_views"),
    path("add-to-cart/<str:id>/", views.AddToCart.as_view(), name="Add to cart"),
    path(
        "remove-from-cart/<str:id>/",
        views.RemoveFromCart.as_view(),
        name="remove-from-cart",
    ),
]
