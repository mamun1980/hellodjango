from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'hellodjango.views.home', name='home'),
    url(r'^latest-user/json/$', 'hellodjango.views.GetUserLatestInfo', name='latest-user-json'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
