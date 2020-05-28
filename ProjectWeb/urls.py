"""
Definition of urls for Projectweb.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [
    # Examples:
    url(r'^$', app.views.home, name='home'),

    url(r'^cart/', include('cart.urls', namespace='cart')),
    url(r'^orders/', include('orders.urls', namespace='orders')),
    url(r'^shop/', include('shop.urls', namespace='shop')),

    url(r'^contact$', app.views.contact, name='contact'),
    url(r'^about$', app.views.about, name='about'),
    url(r'^tort1$', app.views.tort1, name='tort1'),
    url(r'^tort2$', app.views.tort2, name='tort2'),
    url(r'^tort3$', app.views.tort3, name='tort3'),
    url(r'^tort4$', app.views.tort4, name='tort4'),
    url(r'^newpost$', app.views.newpost, name='newpost'),
    url(r'^registration$', app.views.registration, name='registration'),
    url(r'^blog$', app.views.blog, name='blog'),
    url(r'^(?P<parametr>\d+)/$', app.views.blogpost, name='blogpost'),
    url(r'^login/$',

        django.contrib.auth.views.login,
        {
            'template_name': 'app/login.html',
            'authentication_form': app.forms.BootstrapAuthenticationForm,
            'extra_context':
            {
                'title': 'Вход',
                'year': datetime.now().year,
            }
        },
        name='login'),
    url(r'^logout$',
        django.contrib.auth.views.logout,
        {
            'next_page': '/',
        },
        name='logout'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()