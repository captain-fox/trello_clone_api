from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^card/(?P<un>[0-9a-f-]+)$', views.CardDetails.as_view()),
    url(r'^cards/$', views.Cards.as_view()),
    url(r'^board/(?P<id>[0-9]+)$', views.BoardContents.as_view()),
    url(r'^boards/$', views.Tables.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)