#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals


class TitleSearchMixin(object):

    def get_queryset(self):
        # 부모의 get_queryset 으로부터 queryset을 가져오기
        queryset = super(TitleSearchMixin, self).get_queryset()

        # q라는 GET 파라미터 가져우기
        q = self.request.GET.get("q")
        if q:
            # 필터된 쿼리세트 변환
            return queryset.filter(title__icontains=q)
        # q가 지정되지 않으면 그냥 queryset 변환
        return queryset
