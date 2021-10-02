from .import views
from .views import ytube
from django.urls import path
urlpatterns = [
    
    path('home',views.real,name='home'),
    path('',views.home.as_view(),name='realhome'),
    path('create',views.ytube.as_view(),name='ytcreate'),
    path('ythome',views.ythome.as_view(),name = 'ythome'),
    path('HPAGE',views.hpage,name='hpage'),
    path('login',views.loginuser,name = 'login'),
    path('logout',views.logout,name='logoutuser'),
]