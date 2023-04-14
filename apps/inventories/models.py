from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel


# Create your models here.

class Inventory(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name=_("Name"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    purchased_date = models.DateField()
    guarantee_expire_date = models.DateField()

    class Meta:
        ordering = ["guarantee_expire_date"]
        verbose_name = _("Inventory")
        verbose_name_plural = _("Inventories")

    def __str__(self):
        return self.name
