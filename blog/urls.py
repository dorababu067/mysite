from django.conf.urls import url
from .  import views


urlpatterns = [
    
    url(r'^$',views.Index_View,name ='index'),
    url(r'^posts$',views.Post_List_View,name='posts'),
    url(r'^create$',views.Create_Post,name='Create'),
    url(r'^post/(?P<id>\d+)/$',views.Post_Detail_View,name='details'),
    url(r'^registration$',views.Create_User_View,name='registration'),
   	url(r'^login$',views.Login_view,name='login'),
    url(r'^logout$',views.Log_Out,name='logout'),
    url(r'^profil$',views.Profile_View,name='profile'),
    url(r'^profile/update/$',views.Profile_Update,name='update'),
    url(r'^postlike$',views.Like_Post,name='likes'),
    url(r'^post/edit/(?P<id>\d+)/$',views.Post_Edit,name='edit'),
    url(r'^post/delete/(?P<id>\d+)/$',views.Post_Delete,name='delete'),
    

  
]
	# url(r'^profile/$',views.Profile_Edit_View,name='profile'),
    # url(r'^profile$',views.Profile_View,name='profile'),
    # # url(r'^like$',views.like_View,name='like_post'),

    # # 
