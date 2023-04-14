from ckeditor.fields import RichTextField
from django.db import models
from django.utils.translation import gettext_lazy as _
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel


# Create your models here.

class Event(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    location = models.CharField(max_length=100)
    # location = models.PointField()
    start_time = models.DateTimeField(verbose_name=_("Time From"))
    end_time = models.DateTimeField(verbose_name=_("Time To"))
    content = RichTextField(verbose_name=_("Content"))
    image = ImageField(upload_to="events/%Y/%m", verbose_name=_("Image"))

    class Meta:
        verbose_name = _("Event")
        verbose_name_plural = _("Events")

    def __str__(self):
        return self.title
