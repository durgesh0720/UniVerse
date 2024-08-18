from django.urls import path
from . import views
from assignments_manager import views as _views # type: ignore
from attendance_manager import views as attendanceViews #type: ignore

urlpatterns=[
    path('',views.homepage,name='admin-home'),
    path('signup/',views.signupAdmin,name='signup-admin'),
    path('admin-pannel/',views.adminPage,name='adminPage'),
    path('loginAdmin/',views.loginAdmin,name='loginAdmin'),
    path('save-admin/',views.save_admin,name='save-admin'),
    path('login-admin/',views.Admin_login,name='admin-login'),
    path('sign-out/',views.sign_out,name='sign-out'),

                # here now manage assignments

    path('assignment-manager/',_views.assignment_home,name='assignment-home'),
    path('upload-assignment/',_views.upload_assignment,name='upload-assignment'),
    path('save-assignments/',_views.saveAssignments,name="saveAssignments"),
    path('edit-assignment/',_views.editAssignment,name="editAssignment"),
    path('update-assignment/',_views.updateAssignment,name="updateAssignment"),
    path('delete-assignment/',_views.deleteAssignment,name="deleteAssignment"),
    path('show-submissions/',_views.showAssignmentSubmissions,name="studentSubmissions"),
    path('submission-action/',_views.updateStatus,name='submissionaction'),

                # here now manage attendance

    path('attendance-manager/',attendanceViews.attendanceManager,name='attendanceHome'),
    path('attendance-save/',attendanceViews.saveStudentAttendance,name='attendanceSave'),
    path('showStudentAttendanceStatus/',attendanceViews.showStudentAttendanceStatus,name="showStatus"),
]