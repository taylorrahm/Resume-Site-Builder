from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin
import settings

admin.autodiscover()

urlpatterns = patterns('',
	url(r'^$', 'resumes.views.main'),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^media/(.*)$', 'django.views.static.serve',{'document_root': settings.MEDIA_ROOT}),
)
