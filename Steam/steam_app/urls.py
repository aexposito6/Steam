from django.conf.urls import  url
import views
from views import APIUserProfileList, APIUserProfileDetail


urlpatterns = (

    url(r'^register/$', views.register, name  = "register"),
    #url(r'^userprofile/(?P<id_user>\d)/$', views.APIUserProfileList.as_view(), name='user-list'),
    url(r'^userprofile/$', APIUserProfileList.as_view(), name='userprofile-list'),
    url(r'^userprofile/(?P<pk>\d+)/$', APIUserProfileDetail.as_view(), name='userprofile-detail'),

)