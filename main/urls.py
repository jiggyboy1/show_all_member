from django.urls import path
from . import views


urlpatterns = [
    path('',views.home, name="home"),
    path('create/',views.Createmember, name="create"),
    path('member/<str:pk>',views.member, name="member"),
]

