from django.conf.urls import *
from django.contrib.auth import views as auth_views
from django.contrib import admin
from admissions import views
from django.conf import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       #url(r'^$', 'school.views.home', name='home'),
                       # url(r'^blog/', include('blog.urls')),

                       url(r'^admin/', include(admin.site.urls)),
                       #override the default urls
                       url(r'^accounts/password/change/$', auth_views.password_change, name='password_change'),
                       url(r'^accounts/password/change/done/$', auth_views.password_change_done,
                           name='password_change_done'),
                       url(r'^accounts/password/reset/$', auth_views.password_reset, name='password_reset'),
                       url(r'^accounts/password/reset/done/$', auth_views.password_reset_done,
                           name='password_reset_done'),
                       url(r'^accounts/password/reset/complete/$', auth_views.password_reset_complete,
                           name='password_reset_complete'),
                       url(r'^accounts/password/reset/confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
                           auth_views.password_reset_confirm, name='password_reset_confirm'),

                       #and now add the registration urls
                       url(r'^accounts/', include('registration.backends.default.urls')),

                       # Application Form & institution related URLs
                       url(r'^application/apply/$', views.apply, name='apply'),
                       url(r'^institution/(?P<institute_id>\d+)/$', views.institution_details, name='view-institute-details'),
                       url(r'^institution/$', views.institution_list, name='view-all-institutes'),
                       url(r'^institution/(?P<institute_id>\d+)/applications/$', views.get_applications_list, name='view-apps-for-inst'),
                       #url(r'^search/$', views.search_institutes, name='about'),
                       (r'^search/', include('haystack.urls')),
                       # Other URLs
                       url(r'^about/$', views.about, name='about'),
                       url(r'^contact/$', include('contact_form.urls')),

                       # catch-all URL
                       url(r'^$', views.index, name='index'),
)

if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
         'serve',
         {'document_root': settings.MEDIA_ROOT}), )