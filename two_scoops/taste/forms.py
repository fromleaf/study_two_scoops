#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms

from .models import Taster

class TasterForm(forms.ModelForm):

    class Meta:
        model = Taster

    def __init__(self, *args, **kwargs):
        # add form to user attributes
        self.user = kwargs.pop('user')
        super(TasterForm, self).__init__(*args, **kwargs)
