from django.urls import path
from . import views

urlpatterns = [
    path('login',views.login_user,name="login" ),
    path('register',views.resister_user,name='register'),
    path('profile', views.profile, name='profile'),
    path('Edit_profile', views.Edit_profile, name='Edit_profile'),
    path('logout', views.logout_user, name="logout"),

    path('', views.home, name='home')

]
