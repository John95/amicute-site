from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin

from cutedb.views import AuthorizedHomePageView
from cutedb.views import UnauthorizedHomePageView
from cutedb.views import Register
from cutedb.views import CreatePost
from cutedb.views import DisplayPost

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^post/(?P<post_id>\d+)/$', DisplayPost.as_view(), name='display_post'),
    url(r'^post/', CreatePost.as_view(), name='post'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', UnauthorizedHomePageView.as_view(), name='unauthorized_homepage'),
    url(r'^register/', Register.as_view(), name='register'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}, name='login'),
    url(r'^home/$', AuthorizedHomePageView.as_view(), name='authorized_homepage'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'template_name': 'logout.html'}),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
