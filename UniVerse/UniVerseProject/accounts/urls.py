from django.urls import path
from . import views

urlpatterns = [
    path("",views.homepage,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.log_in,name="login"),
    path("saving/",views.saveUsers,name="save"),
    path("user_verified/",views.checkUser,name="checkUser"),
    path("profile",views.profile,name="profile"),
    path("update-profile",views.update_profile,name="update-profile"),
    path("edit-profile/",views.edit_profile,name="edit_profile"),
    path("logout/",views.log_out,name="logout"),
]
