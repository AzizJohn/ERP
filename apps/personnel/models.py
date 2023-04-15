from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from sorl.thumbnail import ImageField

from apps.common.models import TimeStampedModel


# Create your models here.
class StaffType(models.TextChoices):
    STAFF = "Staff"
    INTERN = "Intern"


class Personnel(TimeStampedModel):
    phone = PhoneNumberField(_("Phone number"), max_length=32, unique=True, null=True)
    full_name = models.CharField(_("Full name"), max_length=32, null=True, blank=True)
    position = models.CharField(max_length=50)
    avatar = ImageField(upload_to="users/%Y/%m/", blank=True, null=True)
    email = models.EmailField(_("Email"), blank=True, null=True, unique=True)
    birthday = models.DateField(verbose_name=_("Date of birth"))
    date_of_employment = models.DateField()
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name=_("salary"))
    # internship = models.ForeignKey('internships.Internship', on_delete=models.CASCADE, null=True, blank=True)
    bio = models.TextField(_("Bio"), null=True, blank=True)
    type = models.CharField(verbose_name=_("Staff type"), max_length=20, choices=StaffType.choices,
                            default=StaffType.STAFF)

    def __str__(self):
        return self.full_name

    class Meta:
        app_label = 'personnel'
        verbose_name = _("Personnel")
        verbose_name_plural = _("Personnel")
