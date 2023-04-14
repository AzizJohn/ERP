from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


# Create your models here.
class ProjectStatus(models.TextChoices):
    COURSE_SALE = "In Progres", _("In Progres")
    VIDEO_SALE = "Finished", _("Finished")


class Project(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("Price"))
    start_date = models.DateField(verbose_name=_("Start Date"))
    deadline = models.DateField(verbose_name=_("Deadline"))
    current_status = models.CharField(max_length=30, choices=ProjectStatus.choices, verbose_name=_("Status"))

    class Meta:
        verbose_name = _("Project")
        verbose_name_plural = _("Projects")

    def __str__(self):
        return f"{self.title} - {self.current_status}"
