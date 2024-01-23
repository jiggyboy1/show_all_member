from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('about/',views.about, name="about"),
    path('create/',views.Createmember, name="create"),
    path('login/',views.login_user, name="login"),
    path('member/<str:pk>',views.member, name="member"),
]

