# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r"^$", view=views.TasteListView.as_view()),
    url(regex=r"^(?P<pk>\d+)/$", view=views.TasteDetailView.as_view(), name="detail"),
    url(regex=r"^(?P<pk>\d+)/results/$", view=views.TasteDetailView.as_view(), name="results"),
    url(regex=r"^(?P<pk>\d+)/update/$", view=views.TasteUpdateView.as_view(), name="update")
]