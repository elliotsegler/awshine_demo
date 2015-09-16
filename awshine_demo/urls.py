from django.conf.urls import include, url
from django.contrib import admin

from feedback import urls as feedback_urls

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(feedback_urls))
]
urlpatterns += staticfiles_urlpatterns()