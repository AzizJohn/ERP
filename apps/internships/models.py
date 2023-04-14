from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.common.models import TimeStampedModel


# Create your models here.

class Internship(TimeStampedModel):
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    start_date = models.DateField(verbose_name=_("Start date"))
    finish_date = models.DateField(verbose_name=_("Finish date"))
    num_of_trainee = models.PositiveIntegerField()
    mentor = models.ForeignKey('personnel.Personnel', on_delete=models.CASCADE)
    description = models.CharField(max_length=300)

    def __str__(self):
        return f"{self.title} - {self.mentor.full_name}"

    class Meta:
        verbose_name = _("Internship")
        verbose_name_plural = _("Internships")