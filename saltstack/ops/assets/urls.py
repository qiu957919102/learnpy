from django.conf.urls import url
from assets.views import *

urlpatterns = [
    url(r'^hostGroup/$', hostGroup, name='hostGroup'),
    url(r'^hostGroup/form/$', hostGroupForm, name='hostGroupForm'),
    url(r'^hostGroup/rest/$', HostGroupRest.as_view(), name='hostGroupRest'),
    url(r'^host/$', host, name='host'),
    url(r'^host/form/$', hostForm, name='hostForm'),
    url(r'^host/rest/$', HostRest.as_view(), name='hostRest'),
    url(r'^host/sync/$', hostSync, name='hostSync'),
]
