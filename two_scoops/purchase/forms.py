#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import csv
from io import StringIO

from django import forms

from .models import Purchase, Seller

class PurchaseForm(forms.ModelForm):

    class Meta:
        model = Purchase

    def clean_seller(self):
        seller  = self.cleaned_data["seller"]
        try:
            Seller.objects.get(name=seller)
        except Seller.DoesNotExist:
            msg = "{0} does not exist in purchase #{1}.".format(
                seller,
                self.cleaned_data["purchase_number"]
            )
            raise forms.ValidationError(msg)

        return seller

    def add_csv_purchases(rows):

        rows = StringIO(rows)

        records_added = 0
        errors = []

        # 한 줄당 하나의 dict를 생성. 단 첫 번째 줄은 키 값으로 함
        for row in csv.DictReader(rows, delimiter=",'"):
            # PurchaseForm에 원본 데이터 추가
            form = PurchaseForm(row)
            if form.is_valid():
                form.save()
                records_added += 1
            else:
                errors.append(form.errors)

        return records_added, errors
