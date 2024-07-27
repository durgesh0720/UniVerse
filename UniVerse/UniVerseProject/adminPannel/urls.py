from django.urls import path
from . import views

urlpatterns=[
    path('',views.homepage,name='admin-home'),
    path('signup/',views.signupAdmin,name='signup-admin'),
    # path('admin-pannel/',views.adminPage,name='admin'),
    path('loginAdmin/',views.loginAdmin,name='loginAdmin'),
    path('save-admin/',views.save_admin,name='save-admin'),
    path('login-admin/',views.Admin_login,name='admin-login'),
    path('sign-out/',views.sign_out,name='sign-out')
]