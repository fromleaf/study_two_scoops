#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from core.validators import validate_tasty
from .models import Flavor


class IceCreamOrderForm(forms.Form):
    """
    일반적으로 forms.ModelForm을 이용하면 된다. 하지만
    모든 종류의 폼에서 이와 같은 방식을 적용할 수 있음을 보이기 위해
    forms.Form을 이용했다
    """
    slug = forms.ChoiceField("Flavor")
    toppings = forms.CharField()

    def __init__(self, *args, **kwargs):
        super(IceCreamOrderForm, self).__init__(*args, **kwargs)
        # 선택 가능한 옵션을 (모델의) flavor 필드에서
        # 설정하지 않고 여기서 동적으로 설정했다
        # 필드에서 설정하면 서버를 재시작하지 않고는
        # 폼에 설정 상태를 변경할 수 없기 때문이다.
        self.fields['slug'].choices = [
            (x.slug, x.title) for x in Flavor.objects.all()
        ]

    def clean_slug(self):
        slug = self.cleaned_data['slug']
        if Flavor.objects.get(slug=slug).scoops_remaining <= 0:
            msg = u"Sorry, we are out of that flavor."
            raise forms.ValidationError(msg)

        return slug

    def clean(self):
        cleaned_data = super(IceCreamOrderForm, self).clean()
        slug = cleaned_data.get("slug", "")
        toppings = cleaned_data.get("toppings", "")

        # "too much chocolate" 유효성 검사 예
        if u"chocolate" in slug.lower() and u"chocolate" in toppings.lower():
            msg = u"Your order has too much chocolate."
            raise forms.ValidationError(msg)

        return cleaned_data


class FlavorForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(FlavorForm, self).__init__(*args, **kwargs)
        self.fields["title"].validators.append(validate_tasty)
        self.fields["slug"].validators.append(validate_tasty)

    class Meta:
        model = Flavor
