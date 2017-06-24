# -*- coding: utf-8 -*-

from django.db import models
from django.utils import timezone


from core.models import TimeStampedModel


class Flavor(TimeStampedModel):
    pub_date = models.DateTimeField()


class PublishedManager(models.Manager):
    use_for_related_fields = True

    def published(self, **kwargs):
        return self.filter(pub_date__lte=timezone.now(), **kwargs)


class FlavorReview(models.Model):
    review = models.CharField(max_length=255)
    pub_date = models.DateTimeField()

    # 커스텀 모델 메니저를 여기에 추가
    objects = PublishedManager()
