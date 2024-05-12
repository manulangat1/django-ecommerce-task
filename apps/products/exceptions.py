from rest_framework.exceptions import APIException


class ProductNotFound(APIException):
    status_code = 404
    default_detail = "Product not found"


class CategoryNotFound(APIException):
    status_code = 404
    default_detail = "Category not found"
