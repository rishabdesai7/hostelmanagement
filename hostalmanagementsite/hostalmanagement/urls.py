from django.contrib import admin
from django.urls import path
from hostalmanagement import views
urlpatterns = [
    path('',views.index,name = 'index'),
    path('login',views.login,name = 'login'),
    path('auth',views.auth,name = 'auth'),
    path('sdash',views.dashboard,name = 'dash'),
    path('logout',views.logout,name = 'logout'),
    path('apply',views.apply,name = 'apply'),
    path('application',views.application,name = 'application'),
    path('complaints',views.complaints,name = 'complaints'),
    path('complain',views.complain,name = 'complain'),
    path('contact',views.contact,name = 'contact')
]
