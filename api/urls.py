from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    # get list of all boards (projects) / add new board / edit existing boards
    url(r'^boards/$', views.Boards.as_view()),
    # get list of tables from board with ID ...
    url(r'^board/(?P<id>[0-9]+)/tables/$', views.BoardTables.as_view()),
    # get list of all tables / add new table / edit existing tables
    url(r'^tables/$', views.Tables.as_view()),
    # get list of cards form table with ID ...
    url(r'^table/(?P<tableid>[0-9]+)/cards/$', views.TableContents.as_view()),
    # get list of all cards / add new card / edit existing cards
    url(r'^cards/$', views.Cards.as_view()),
    # operate on an instance of specific card / put, delete, etc...
    url(r'^card/(?P<cardid>[0-9a-f-]+)$', views.CardDetails.as_view()),
    # get list of archived cards / put a card to archive
    # url(r'^archive/$', views.ArchiveCards.as_view()),
    # get list of all users and their credentials, cards, etc...
    url(r'^users/$', views.UserList.as_view()),
    # get specific user and his credentials, cards, etc...
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
