from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # access all boards (projects) / add new board
    url(r'^boards/$', views.Boards.as_view()),
    # get list of tables in board with ID ...
    url(r'^board/(?P<id>[0-9]+)/tables/$', views.BoardTables.as_view()),
    # get list of all tables in all boards / add new table
    url(r'^tables/$', views.Tables.as_view()),
    # get list of cards in a table with ID ...
    url(r'^table/(?P<tableid>[0-9]+)/cards/$', views.TableContents.as_view()),
    # get list of all cards / add new card
    url(r'^cards/$', views.Cards.as_view()),
    # operate on an instance of specific card / put, delete, etc...
    url(r'^card/(?P<cardid>[0-9a-f-]+)$', views.CardDetails.as_view()),
    # get list of archived cards / put a card to archive
    url(r'^archive/$', views.ArchiveCards.as_view()),
    # get list of all users and their credentials, cards, etc...
    url(r'^users/$', views.UserList.as_view()),
    # get specific user and his credentials, cards, etc...
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
