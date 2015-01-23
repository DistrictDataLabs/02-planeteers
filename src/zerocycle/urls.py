from django.conf.urls import patterns, include, url

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^index.html', 'zerocycle.views.home', name='home'),
    url(r'^charts.html', 'zerocycle.views.charts', name='charts'),
    url(r'^tables.html', 'zerocycle.views.tables', name='tables'),
    url(r'^forms.html', 'zerocycle.views.forms', name='forms'),
    
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
  urlpatterns += static(settings.STATIC_URL, 
                          document_root=settings.STATIC_ROOT)
  urlpatterns += static(settings.MEDIA_URL, 
                          document_root=settings.MEDIA_ROOT)