from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField


User = get_user_model()
from apps.common.models import TimeStampedUUIDModel

# Create your models here.


class Profile(TimeStampedUUIDModel):
    user = models.OneToOneField(User, related_name="profile", on_delete=models.CASCADE)
    phone_number = PhoneNumberField(max_length=30)
    country = CountryField(
        verbose_name=_("Country"), default="KE", blank=True, null=True
    )
    city = models.CharField(
        verbose_name=_("City"), blank=True, null=True, max_length=180
    )

    # TODO: come and set the is_seller and is_buyer
    """
    if time allows, implement rating functionality here
    """

    def __str__(self) -> str:
        return f"{self.user}'s profile"
