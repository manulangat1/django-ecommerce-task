from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedUUIDModel
from autoslug import AutoSlugField

"""
Custom manager that returns all the products that are currently being sold. 

"""


class ProductSellingManager(models.Manager):

    def get_queryset(self) -> models.QuerySet:
        return super(ProductSellingManager, self).get_queryset().filter(is_selling=True)


class Product(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Name"), max_length=45, unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.PositiveBigIntegerField(null=False, blank=False)
    # each time product is sold, reduce this by 1 and when it gets to 0 set the is_selling to False
    quantity = models.PositiveIntegerField(default=0)
    discount_price = models.PositiveBigIntegerField(null=False, blank=False, default=0)
    is_discounted = models.BooleanField(default=False)
    slug = AutoSlugField(populate_from="name", unique=True, always_update=True)
    # you can have a field for the tax, ie a seller can input the price without tax and the total amount is computed from here.

    photo = models.ImageField(verbose_name=_("Main photo"), null=True, blank=True)
    # allow a seller to remove
    is_selling = models.BooleanField(default=True)

    # the no of times it has been viewed by users

    # views = models.PositiveIntegerField(verbose_name=_("Views"), default=0)

    objects = models.Manager()

    selling = ProductSellingManager()

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def save(self, *args, **kwargs):
        self.name = str.title(self.name)
        # self.description = str.description(self.description)
        super(Product, self).save(*args, **kwargs)

    @property
    def final_product_price(self):
        if self.is_discounted:
            return self.discount_price
        return self.price


class Category(TimeStampedUUIDModel):
    name = models.CharField(verbose_name=_("Name"), max_length=45, unique=True)
    description = models.TextField(blank=True, null=True)

    products = models.ManyToManyField(Product)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
