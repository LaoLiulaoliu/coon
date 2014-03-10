from django.conf.urls import patterns, include, url

#from django.contrib import admin
#admin.autodiscover()
from critique import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'coon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^suggest.html', views.suggest, name='suggest'),
    url(r'^thanks.html', views.thanks, name='thanks'),

    url(r'^company/', include('critique.urls', namespace='critique')),
    url(r'^accounts/', include('apps.accounts.urls')),

    url(r'^$', views.homepage, name="homepage"),
)
