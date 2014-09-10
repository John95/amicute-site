from django.conf.urls import patterns, include, url

from django.contrib import admin

from cutedb.views import AuthorizedHomePageView
from cutedb.views import UnauthorizedHomePageView
from cutedb.views import Register

admin.autodiscover()

urlpatterns = patterns('',

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', UnauthorizedHomePageView.as_view(), name='unauthorized_homepage'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^home/$', AuthorizedHomePageView.as_view(), name='authorized_homepage'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
)
