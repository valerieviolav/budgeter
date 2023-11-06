from django.urls import path

from . import views

app_name = 'auth'
urlpatterns = [
    path('signin/', views.signin, name='signin'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]