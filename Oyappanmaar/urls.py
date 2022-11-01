from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('check/', views.check, name='check'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_user/signup/', views.signup, name='signup'),
]
