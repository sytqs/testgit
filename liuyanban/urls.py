"""liuyanban URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout
from django.contrib.auth.views import password_change,password_change_done
from messageboard.views import main, register_page, register_success, msg_post_page

admin.autodiscover()

urlpatterns = [
    url(r'^main/$', main),
    url(r'main/post/$', msg_post_page),
    url(r'^main/register/$', register_page),
    url(r'accounts/login/$', login),
    url(r'main/logout/$', logout, {'next_page': '/main/'}),
    url(r'^main/password/change/$', password_change,{'template_name':'registration/password_change.html'}),
    url(r'main/password/change/done/$', password_change_done,{'template_name':'registration/password_change_success.html'}),
    url(r'^main/register/success/$', register_success),
    url(r'^admin/', include(admin.site.urls)),
]
