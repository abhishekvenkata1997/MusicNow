

from django.urls import path
from django.conf.urls import url
from . import views


app_name = 'music'

urlpatterns = [

 # music/
    path('',views.IndexView.as_view(),name = 'index'),

    #music/songs/
    path('songs/',views.IndexView1.as_view(),name = 'index1'),

    #music/search/q?=
    path('search/',views.search,name = 'search'),

    #music/login/
    path('login/',views.loginuser ,name='login'),

    #music/id/favorite
    url(r'^(?P<song_id>[0-9]+)/favorite/$',views.favorite,name = 'favorite'),

    #music/register/
     path('register/',views.UserFormView.as_view(),name = 'register'),

    #music/logout/
    path('logout/',views.logoutuser,name = 'logout'),

     #music/id/
    url(r'^(?P<pk>[0-9]+)/$',views.DetailView.as_view(),name = 'detail'),

    #music/album/add/
    url(r'album/add/$',views.AlbumCreate.as_view(),name = 'album_add'),

    #music/song/add/
    url(r'song/add/$',views.SongCreate.as_view(),name = 'song_add'),

    #music/album/2/
    url(r'album/(?P<pk>[0-9]+)/$',views.AlbumUpdate.as_view(),name = 'album_update'),

    #music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$',views.AlbumDelete.as_view(),name = 'album_delete')
]

