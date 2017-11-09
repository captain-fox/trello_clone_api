from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^card/(?P<un>[0-9a-f-]+)$', views.CardDetails.as_view()),
    url(r'^cards/$', views.Cards.as_view()),
    url(r'^board/(?P<id>[0-9]+)$', views.BoardDetails.as_view()),
    url(r'^boards/$', views.Boards.as_view()),
]