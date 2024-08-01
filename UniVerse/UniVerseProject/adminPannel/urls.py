from django.urls import path
from . import views
from assignments_manager import views as _views # type: ignore
urlpatterns=[
    path('',views.homepage,name='admin-home'),
    path('signup/',views.signupAdmin,name='signup-admin'),
    path('admin-pannel/',views.adminPage,name='adminPage'),
    path('loginAdmin/',views.loginAdmin,name='loginAdmin'),
    path('save-admin/',views.save_admin,name='save-admin'),
    path('login-admin/',views.Admin_login,name='admin-login'),
    path('sign-out/',views.sign_out,name='sign-out'),
    path('assignment-manager/',_views.assignment_home,name='assignment-home'),
    path('upload-assignment/',_views.upload_assignment,name='upload-assignment'),
    
]