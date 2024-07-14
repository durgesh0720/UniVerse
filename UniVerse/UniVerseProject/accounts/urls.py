from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="home"),
    path("signup",views.signup,name="signup"),
    path("login",views.login,name="login"),
    path("save_user",views.saveUsers,name="save"),
    path("checkUser",views.checkUser,name="checkUser"),
]
