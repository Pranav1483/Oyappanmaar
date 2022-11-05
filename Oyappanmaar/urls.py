from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('new_user/', views.new_user, name='new_user'),
    path('new_user/signup/', views.add_user, name='add_user'),
    path('check/logout/', views.logout, name='logout'),
    path('check/addpersonal/', views.addp, name='addp'),
    path('check/addpersonal/addpersonalfinal/', views.addpfinal, name='addpfinal'),
    path('check/addpublic/', views.addP, name='addP'),
    path('check/addpublic/addpublicfinal/', views.addPfinal, name='addPfinal'),
    path('forgot/', views.forgot, name='forgot'),
    path('forgot/forgotp/', views.forgotp, name='forgotp'),
    path('forgot/forgotp/resetp/', views.resetp, name='resetp'),
    path('forgot/forgotp/resetp/newp/', views.newp, name='newp'),
]
