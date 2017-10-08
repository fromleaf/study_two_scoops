#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import IceCreamStore


class IceCreamStoreCreateForm(forms.ModelForm):

    class Meta:
        model = IceCreamStore
        fields = ("title", "block_address")


class IceCreamStoreUpdateForm(IceCreamStoreCreateForm):

    def __init__(self, *args, **kwargs):
        # 필드 오버로드가 이루어지지 이전에
        # 원래의 __init__ 메서드를 호출한다
        super(IceCreamStoreUpdateForm, self).__init__(*args, **kwargs)
        self.fields["phone"].required = True
        self.fields["description"].required = True

    class Meta(IceCreamStoreCreateForm.Meta):
        fields = ("title", "block_address", "phone", "description")
