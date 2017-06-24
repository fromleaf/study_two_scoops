# -*- coding: utf-8 -*-

from django.db import models


class TimeStampedModel(models.Model):
    """
    'created'와 'modified' 필드를 자동으로 업데이트 해주는 추상화 기반 클래스 모델
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
