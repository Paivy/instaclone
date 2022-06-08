from django.urls import path,re_path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.urls import path



urlpatterns =[
    path('', views.index,name='index'),
    path('post',views.post_picture,name='post'),
    # path('myprofile',views.profile,name='profile'),
    path('profile',views.make_profile,name='profile'),
    path('comment/<image_id>', views.comment, name="comment"),
    path('search', views.search_profile, name="search_profile"),
    path('like/<post_id>', views.like, name="like"),
    




    path('login-user', views.login_user, name="login"),
    path('logout-user', views.logout_user, name="logout"),
    path('register-user', views.register_user, name="register"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)