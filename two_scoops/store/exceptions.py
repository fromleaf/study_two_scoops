# -*- coding: utf-8 -*-

from django.core.exceptions import ObjectDoesNotExist, ValidationError


class OutOfStock(ObjectDoesNotExist):
    pass


class CorruptedDatabase(ValidationError):
    pass
