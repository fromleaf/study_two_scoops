# -*- coding: utf-8 -*-

from cached_property import cached_property

from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import (
    ListView, UpdateView, TemplateView, DetailView, CreateView
)
from django.core.urlresolvers import reverse

from braces.views import LoginRequiredMixin
from store.exceptions import OutOfStock

from .models import Flavor, Tasting
from .tasks import update_users_who_favorited


def list_flavor_line_item(sku):
    try:
        return Flavor.objects.get(sku=sku, quantity__gt=0)

    except Flavor.DoesNotExist:
        msg = "We are out of {0}".format(sku)
        raise OutOfStock(msg)


def list_any_line_item(model, sku):
    try:
        return model.objects.get(sku=sku, quantity__gt=0)
    except ObjectDoesNotExist:
        msg = "We are out of {0}".format(sku)
        raise OutOfStock(msg)


class TasteListView(ListView):
    model = Tasting


class TasteDetailView(DetailView):
    model = Tasting


class TasteResultView(TasteDetailView):
    template_name = "taste/results.html"


class TasteUpdateView(UpdateView):
    model = Tasting

    def get_success_url(self):
        return reverse("taste:detail", kwargs={"pk": self.object.pk})


class FreshFruitMixin(object):

    @cached_property
    def likes_and_favorites(self):
        likes = self.object.likes()
        favorites = self.object.favorites()
        return {
            "likes": likes,
            "favorites": favorites,
            "favorites_count": favorites.count(),
        }

    def get_context_data(self, **kwargs):
        context = super(FreshFruitMixin, self).get_context_data(**kwargs)
        context["has_fresh_fruit"] = True
        return context


class FruityFlavorView(FreshFruitMixin, TemplateView):
    template_name = "taste/fruity_flavor.html"


class FlavorDetailView(LoginRequiredMixin, DetailView):
    model = Flavor


class FlavorCreateView(LoginRequiredMixin, CreateView):
    model = Flavor
    fields = ('title', 'slug', 'scoops_remaining')

    def form_valid(self, form):
        update_users_who_favorited(
            instances=self.object,
            favorites=self.likes_and_favorites['favorites']
        )
        return super(FlavorCreateView, self).form_valid(form)
