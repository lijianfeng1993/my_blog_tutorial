"""my_blog URL Configuration

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
from django.conf.urls import url, patterns, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
  # url(r'^$','artical.views.home'),
  # url(r'^(?P<my_args>\d+)/$','artical.views.detail', name = 'detail'),
  # url(r'^test/$','artical.views.test'),
    url(r'^$', 'artical.views.home', name = 'home'),
    url(r'^(?P<id>\d+)/$', 'artical.views.detail', name = 'detail'),
    url(r'^archives/$', 'artical.views.archives', name = 'archives'),
    url(r'^aboutme/$', 'artical.views.about_me', name = 'about_me'),
    url(r'^(?P<tag>\w+)/$', 'artical.views.search_tag', name = 'search_tag'),
    url(r'^feed/$', 'artical.views.RSSFeed', name = "RSS"), 
]
