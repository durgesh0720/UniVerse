from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="home"),
    path("signup",views.signup,name="signup"),
    path("login",views.log_in,name="login"),
    path("save_user",views.saveUsers,name="save"),
    path("checkUser",views.checkUser,name="checkUser"),
    path("profile",views.profile,name="profile"),
    path("update-profile",views.update_profile,name="update-profile"),
    path("logout/",views.log_out,name="logout"),
]
