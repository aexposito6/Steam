"""Steam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.auth.views import login, logout
from steam_app import views
from django.conf.urls import url, include

urlpatterns = (
    url(r'^$', login, name='mainpage'),
    url(r'^register/$', views.register, name='register'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/profile/$', views.mainpage, name='mainpage'),
    url(r'^game/$', views.games, name='game'),
    url(r'^user/$', views.user, name='user'),
    url(r'^change/game/(?P<id_game>\d)/$', views.change_game,  name='change_game'),
    url(r'^change/game/(?P<id_game>\d)/delete/$', views.delete_game,  name='delete_game'),
    url(r'^change/user/(?P<id_user>\d)/$', views.change_user, name='change_user'),
    url(r'^change/user/(?P<id_user>\d)/delete/$', views.delete_user, name='delete_user'),
    url(r'^list/games/$', views.print_games, name='print_game'),
    url(r'^list/users/$', views.print_users, name='print_users'),
    url(r'^change/game/done/$', views.after_change_game, name='after_change_game'),
    url(r'^change/user/done/$', views.after_change_user, name='after_change_user'),
    url(r'^game/sent/$', views.after_game, name='game_sent'),
    url(r'^user/sent/$', views.after_user, name='user_sent'),
    url(r'^logout/$', logout, {'template_name': 'logout.html'}, name='logout'),
    url(r'^admin/', admin.site.urls),

)
