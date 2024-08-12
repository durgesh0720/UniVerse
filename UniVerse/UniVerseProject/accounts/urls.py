from django.urls import path
from . import views
from assignments_manager import views as _views #type: ignore
from attendance_manager import views as attendance_views # type: ignore

urlpatterns = [

                # Here User Accounts Manage URL

    path("",views.homepage,name="home"),
    path("signup/",views.signup,name="signup"),
    path("login/",views.log_in,name="login"),
    path('welcome/',views.welcomepage,name="welcomepage"),
    path("saving/",views.saveUsers,name="save"),
    path("user_verified/",views.checkUser,name="checkUser"),
    path("profile",views.profile,name="profile"),
    path("update-profile",views.update_profile,name="update-profile"),
    path("edit-profile/",views.edit_profile,name="edit_profile"),
    path("logout/",views.log_out,name="logout"),
    path("dashboard/",views.dashboard,name="dashboard_url"),

                # Here Assignment manage URL

    path("show-assignments/",_views.showAssignmentStudent,name="showAssignmentStudent"),
    path("save-assignment/",_views.saveStudentAssignment,name="saveStudentAssignment"),

                # Here Attendance manage URL

    path("show-attendance/",attendance_views.student_ShowAttendanceStatus,name="showAttendance")
]
