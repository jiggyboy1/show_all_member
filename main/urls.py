from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('create/',views.Createmember, name="create"),
    path('login/',views.login_user, name="login"),
    path('logout/',views.logout_user, name="logout"),
    path('register/',views.register_user, name="register"),
    path('member/<str:pk>',views.member, name="member"),
    path('delete_member/<str:pk>',views.delete_member, name="delete_member"),
]

