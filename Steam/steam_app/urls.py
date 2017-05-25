from django.conf.urls import  url
import views
from views import APIUserProfileList, APIUserProfileDetail


urlpatterns = (
    url(r'^$', views.api_page, name='api_page'),
    url(r'^userprofile/$', APIUserProfileList.as_view(), name='userprofile-list'),
    url(r'^userprofile/(?P<pk>\d+)/$', APIUserProfileDetail.as_view(), name='userprofile-detail'),
    url(r'^game/$', views.APIGameList.as_view(), name='game-list'),
    url(r'^game/(?P<pk>\d+)/$', views.APIGameDetail.as_view(), name='game-detail'),
    url(r'^achievement/$', views.APIAchievementList.as_view(), name='achievement-list'),
    url(r'^achievement/(?P<pk>\d+)/$', views.APIAchievementDetail.as_view(), name='achievement-detail'),
    url(r'^clan/$', views.APIClanList.as_view(), name='clan-list'),
    url(r'^clan/(?P<pk>\d+)/$', views.APIClanDetail.as_view(), name='clan-detail'),
)