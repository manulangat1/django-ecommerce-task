from . import views
from django.urls import path

urlpatterns = [
    path("add-to-cart/<str:id>/", views.AddToCart.as_view(), name="Add to cart")
]
