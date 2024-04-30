from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListAllProductAPIView.as_view(), name="list_all_products")
]
