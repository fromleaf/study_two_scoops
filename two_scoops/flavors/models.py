# flavors/models.py
from django.core.urlresolvers import reverse
from django.db import models

from core.models import TastyTitleAbstractModel


class Flavor(TastyTitleAbstractModel):
    name = models.CharField(default='', null=False)
    flavor = models.CharField(default='', null=False)
    title = models.CharField(default='', null=False)
    slug = models.SlugField()
    scoops_remaining = models.IntegerField(default=0)

    def get_absolute_url(self):
        return reverse("flavors:detail", kwargs={"slug": self.slug})
