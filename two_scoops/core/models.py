# -*- coding: utf-8 -*-

from django.db import models

from .validators import validate_tasty


class TimeStampedModel(models.Model):
    """
    'created'와 'modified' 필드를 자동으로 업데이트 해주는 추상화 기반 클래스 모델
    """
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ModelFormFailureHistory(models.Model):
    form_data = models.TextField()
    model_data = models.TextField()


class TastyTitleAbstractModel(models.Model):
    title = models.CharField(max_length=255, validators=[validate_tasty])

    class Meta:
        abstract = True
