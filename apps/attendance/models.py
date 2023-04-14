from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.common.models import TimeStampedModel
from apps.personnel.models import Personnel


# Create your models here.

class Attendance(TimeStampedModel):
    personnel = models.ForeignKey(Personnel, on_delete=models.CASCADE, related_name="attendances")
    # work_start_time = models.TimeField(default=datetime.time(hour=10, minute=0))
    # arrival_time = models.TimeField()
    lateness_time = models.DurationField(null=True, blank=True, verbose_name=_("Lateness time"))
    is_absent = models.BooleanField(default=False)

    # @property
    # def lateness_time(self):
    #     if self.arrival_time > self.work_start_time:
    #         lateness = self.arrival_time - self.work_start_time
    #         return lateness.total_seconds() // 60
    #     else:
    #         return 0

    def __str__(self):
        return f"{self.personnel.full_name} - {self.lateness_time}"

    class Meta:
        verbose_name = _("Attendance")
        verbose_name_plural = _("Attendances")
