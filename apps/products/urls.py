from django.urls import path
from . import views

urlpatterns = [
    path("", views.ListAllProductAPIView.as_view(), name="list_all_products"),
    path("create/", views.CreateProductApiView.as_view(), name="create_product"),
    path("<str:id>/", views.GetProductDetail.as_view(), name="get_product_detail"),
]
