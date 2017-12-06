from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^boards/$', views.Boards.as_view()),
    url(r'^board/(?P<id>[0-9]+)/tables/$', views.BoardTables.as_view()),
    url(r'^tables/$', views.Tables.as_view()),
    url(r'^table/(?P<tableid>[0-9]+)/cards/$', views.TableContents.as_view()),
    url(r'^card/(?P<cardid>[0-9a-f-]+)$', views.CardDetails.as_view()),
    url(r'^cards/$', views.Cards.as_view()),
    url(r'^archive/$', views.ArchiveCards.as_view()),
    url(r'^users/$', views.UserList.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
