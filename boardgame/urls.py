"""boardgame URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, patterns, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.conf import settings

import main.views
import user.urls

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^user/', include('user.urls')),
    url(r'^tictactoe/', include('tictactoe.urls')),
    url(r'^$', main.views.home, name='boardgames_home'),
    url(r'^login/$', auth_views.login,
        {'template_name': 'login.html'}, name='boardgames_login'),
    url(r'^logout/$', auth_views.logout,
        {'next_page': 'boardgames_home'}, name='boardgames_logout')
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += patterns('',
        url(r'^__debug__/', include(debug_toolbar.urls)),
    )
