
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
    path('admin-pannel/',include('adminPannel.urls')),
    path('assignment/',include('assignments_manager.urls')),
    path('attendanceManager/',include('attendance_manager.urls')),
    path('social-stream/',include('socialStream.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)