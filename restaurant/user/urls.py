from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('user/?P<pk>\d+/profile/', views.profile, name='profile'),
    # path('user/(?P<pk>\d+)/prodile/update',),
    # path('user/(?P<pk>\d+)/prfile/pwd',),
    path('logout/', views.logout, name='logout'),
]