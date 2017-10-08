#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.exceptions import ValidationError


def validate_tasty(value):
    """
    단어가 'Tasty'로 시작하지 않으면 ValidationError를 일으킨다.
    :param value:
    :return:
    """
    if not value.startswith("Tasty"):
        msg = "Must start with Tasty"
        raise ValidationError(msg)