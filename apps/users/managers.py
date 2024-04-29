from django.contrib.auth.base_user import BaseUserManager
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.utils.translation import gettext_lazy as _


class CustomUserManager(BaseUserManager):

    def email_validator(self, email):
        try:
            validate_email(email)
        except ValidationError:
            raise ValueError(_("You must provide a valid email address"))

    def create_user(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        if not username:
            raise ValueError(_("Users must submit a username"))
        if not first_name:
            raise ValueError(_("Users must submit a first_name"))
        if not last_name:
            raise ValueError(_("Users must submit a last_name"))
        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Email must be provided"))

        user = self.model(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            **extra_fields
        )
        user.set_password(password)
        extra_fields.setdefault("is_staff", "False")
        extra_fields.setdefault("is_superuser", "False")
        """
          In a production instance, this field should be False by default and should be updated by
           1. An email being sent to the user on sign up that has a link that a user clicks on and sets this to true. 
           2. Implementing an otp that gets sent to a users phone number,  the user inputs this and it is updated if true
        """
        extra_fields.setdefault("is_active", "True")
        user.save(using=self._db)
        return user

    def create_superuser(
        self, username, first_name, last_name, email, password, **extra_fields
    ):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Super users must have is_staff=True"))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Super users must have is_superuser=True"))

        if not password:
            raise ValueError("Super users must have  a password")

        if email:
            email = self.normalize_email(email)
            self.email_validator(email)
        else:
            raise ValueError(_("Admin: Email must be provided"))

        user = self.create_user(
            username, first_name, last_name, email, password, **extra_fields
        )
        user.save(using=self._db)
        return user
