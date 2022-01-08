from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('teachers/',views.teacher, name='profile'),
    path('account/', views.account, name='account'),
    path('login/',views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
    path('account/edit', views.editaccount, name='edit-account'),
    path('teachers/<str:pk>', views.teacher_d, name='profile_d'),

]