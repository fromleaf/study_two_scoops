from django.db import models


class Purchase(models.Model):
    name = models.CharField(default='', null=False)


class Seller(models.Model):
    name = models.CharField(default='', null=False)