# -*- coding: utf-8 -*-

from django.core.urlresolvers import reverse
from django.db import models


class Store(models.Model):
    title = models.CharField(max_length=100)


class IceCreamStore(models.Model):
    title = models.CharField(max_length=100)
    block_address = models.TextField()
    phone = models.CharField(max_length=20, blank=True)
    description = models.TextField(blank=True)

    def get_absolute_url(self):
        return reverse("store_detail", kwargs={"pk": self.pk})
