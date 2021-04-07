from django.db.models.signals import pre_delete
from django.dispatch import receiver

from orders.models import Order
from .models import Sale

@receiver(pre_delete, sender=Sale)
def pre_delete_change_active_order(sender, instance, **kwargs):
	obj = instance.order
	obj.active = False
	obj.save()