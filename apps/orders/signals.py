import logging
from django.db.models.signals import post_save
from django.http import HttpResponse

from django.dispatch import receiver
from apps.products.models import Product

logger = logging.getLogger(__name__)


@receiver(post_save, sender=Product)
def set_to_is_selling_to_false_when_product_qty_zero(
    sender, instance, created, **kwargs
):
    print("created")
    logger.info(f"{instance} saved and number is {instance.quantity}")
    if instance.quantity == 0:
        if instance.is_selling:
            instance.is_selling = False
            instance.save()
            logger.info("set to 0 success")
        # return HttpResponse("The products is now not selling")
    else:
        if instance.is_selling is False:
            instance.is_selling = True
            instance.save()
        logger.info(
            f"Quantity for {instance} is {instance.quantity}. No change needed."
        )
