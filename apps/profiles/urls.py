from django.urls import path
from . import views


urlpatterns = [path("me/", views.GetProfileAPIView.as_view(), name="my-profile-view")]
