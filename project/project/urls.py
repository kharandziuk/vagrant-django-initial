from django.conf.urls import patterns, include, url
from django.contrib import admin

from views import HelloView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', HelloView.as_view(), name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
