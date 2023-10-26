from django.urls import path
from . import views 


urlpatterns = [
    path('signup/', views.Signup .as_view()),
    path('login/', views.LoginView .as_view()),
    path('user/', views.UserView .as_view()),
    path('logout/', views.LogoutView .as_view()),

]