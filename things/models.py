from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.translation import gettext as _

class Thing(models.Model):
    name = models.CharField(
        unique=True,
        blank=False,
        max_length=30,
        verbose_name=_('Name')
    )
    description = models.CharField(
        blank=True,
        max_length=120,
        verbose_name=_('Description')
    )
    quantity = models.IntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(100)],
        verbose_name=_('Quantity')
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = _('Thing')
        verbose_name_plural = _('Things')