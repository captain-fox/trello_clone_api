from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^getTablesFromBoardWithID/(?P<id>[0-9]+)$', views.BoardContents.as_view()),
    url(r'^getOrPostListOfBoards/$', views.Boards.as_view()),
    url(r'^getSpecificCardWithID/(?P<un>[0-9a-f-]+)$', views.CardDetails.as_view()),
    url(r'^getOrPostListOfCards/$', views.Cards.as_view()),
    url(r'^getCardsFromTableWithID/(?P<id>[0-9]+)$', views.TableContents.as_view()),
    url(r'^getOrPostListOfTables/$', views.Tables.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)