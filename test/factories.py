import factory
from apps.profiles.models import Profile
from django.db.models.signals import post_save

from faker import Factory as FakerFactory
from ecomerce.settings.base import AUTH_USER_MODEL

faker = FakerFactory.create()


@factory.django.mute_signals(post_save)
class ProfileFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory("tests.factories.UserFactory")
    phone_number = factory.lazy_attribute(lambda x: faker.phone_number())
    country = factory.LazyAttribute(lambda x: faker.country_code())
    city = factory.LazyAttribute(lambda x: faker.city())

    class Meta:
        model = Profile


@factory.django.mute_signals(post_save)
class UserFactory(factory.django.DjangoModelFactory):
    first_name = factory.lazy_attribute(lambda x: faker.first_name())
    last_name = factory.lazy_attribute(lambda x: faker.last_name())
    username = factory.lazy_attribute(lambda x: faker.first_name())
    email = factory.lazy_attribute(lambda x: f"emmanuel@kipchirchirlangat.com")
    password = factory.lazy_attribute(lambda x: faker.password())
    # country = factory.LazyAttribute(lambda x: faker.country_code())
    # city = factory.LazyAttribute(lambda x: faker.city())

    is_active = True
    is_staff = False

    class Meta:
        model = AUTH_USER_MODEL

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        manager = cls._get_manager(model_class)
        if "is_superuser" in kwargs:
            return manager.create_superuser(*args, **kwargs)
        else:
            return manager.create_user(*args, **kwargs)
