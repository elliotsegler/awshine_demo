from __future__ import unicode_literals

from django.conf.urls import patterns, url

from .views import HomePageView
from .views import FeedbackFormView

urlpatterns = [
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^feedback$', FeedbackFormView, name='feedback'),
]