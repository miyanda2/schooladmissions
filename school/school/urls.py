from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'school.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #override the default urls
                       url(r'^accounts/password/change/$',
                           auth_views.password_change,
                           name='password_change'),
                       url(r'^accounts/password/change/done/$',
                           auth_views.password_change_done,
                           name='password_change_done'),
                       url(r'^accounts/password/reset/$',
                           auth_views.password_reset,
                           name='password_reset'),
                       url(r'^accounts/password/reset/done/$',
                           auth_views.password_reset_done,
                           name='password_reset_done'),
                       url(r'^accounts/password/reset/complete/$',
                           auth_views.password_reset_complete,
                           name='password_reset_complete'),
                       url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm,
                           name='password_reset_confirm'),

                       #and now add the registration urls
                       url(r'^accounts/', include('registration.backends.default.urls')),
)
