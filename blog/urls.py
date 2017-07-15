from django.conf.urls import url

from blog.views import detail, tag, home, about, contact

urlpatterns = [
    url(r'^$', home),
    url(r'^p/(?P<key>[\w-]+)/$', detail),
    url(r'^t/(?P<key>[\w-]+)/$', tag),
    url(r'^about/$', about),
    url(r'^contact/$', contact),
    # url(r'^$', home),
]
