from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^cards/$', views.Cards.as_view()),
    url(r'^boards/$', views.Boards.as_view()),
    url(r'^getAllForBoardWithID/(?P<id>[0-9]+)$', views.ForBoard.as_view()),
    # url(r'^pass/(?P<pk>[0-9]+)/$', views.PassDetails.as_view()),
    # url(r'^pass/(?P<pk>[0-9a-f-]+)$', views.PassDetails.as_view()),
]