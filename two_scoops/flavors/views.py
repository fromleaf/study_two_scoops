# flvors/views.py
import json

from braces.views import LoginRequiredMixin
from core.models import ModelFormFailureHistory
from django.contrib import messages
from django.core import serializers
from django.views.generic import CreateView, UpdateView, DetailView

from .models import Flavor
from .forms import FlavorForm


class FlavorActionMixin(object):

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(FlavorActionMixin, self).form_valid(form)

    def form_invalid(self, form):
        """실패 내역을 확인하기 위해 유효성 검사에 실패한 폼과 모델을 저장"""
        form_data = json.dump(form.cleaned_data)
        model_data = serializers.serialize("json", [form.instance])[1:-1]

        ModelFormFailureHistory.objects.create(
            form_data=form_data,
            model_data=model_data
        )
        return super(FlavorActionMixin, self).form_invalid(form)


class FlavorCreateView(LoginRequiredMixin, FlavorActionMixin, CreateView):
    success_msg = "created"
    form_class =  FlavorForm


class FlavorUpdateView(LoginRequiredMixin, FlavorActionMixin, UpdateView):
    success_msg = "updated"
    form_class = FlavorForm


class FlavorDetailView(DetailView):
    model = Flavor
