from django.conf.urls import url
from api import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework.authtoken import views as rf_views

urlpatterns = [

    # superusers:

    # admin
    # adminapipass

    # regular users:

    # stanislaw
    # apipassword

    # robert
    # apipassword

    # http POST 127.0.0.1:8000/authorise/ username='stan' password='apipassword'
    # http GET 127.0.0.1:8000/***/ 'Authorization: Token your_token_value'

    # Obtain auth token
    url(r'^authorise/', rf_views.obtain_auth_token),
    # get list of all boards (projects) / add new board
    url(r'^boards/$', views.Boards.as_view()),
    # get list of tables from board with ID ...
    url(r'^board/(?P<id>[0-9]+)/tables/$', views.BoardTables.as_view()),
    # get list of all tables / add new table / edit existing tables
    url(r'^tables/$', views.Tables.as_view()),
    # get list of cards form table with ID ...
    url(r'^table/(?P<tableid>[0-9]+)/cards/$', views.TableContents.as_view()),
    # get list of all cards / add new card / edit existing cards / delete card
    url(r'^cards/$', views.Cards.as_view()),
    # get an instance of specific card
    url(r'^card/(?P<cardid>[0-9a-f-]+)$', views.CardDetails.as_view()),
    # get list of comments / add comment
    # url(r'^comments/$', views.Comments.as_view()),
    # edit comment / delete comment
    # url(r'^comment/(?P<comment_id>[0-9a-f-]+)$', views.Comments.as_view()),

    # get list of archived cards / put a card to archive
    url(r'^archive/(?P<cardid>[0-9a-f-]+)$', views.ArchiveCards.as_view()),
    # get list of all users and their credentials, cards, etc...
    url(r'^users/$', views.UserList.as_view()),
    # get specific user and his credentials, cards, etc...
    url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
