from django.shortcuts import render,redirect,get_list_or_404,get_object_or_404
from django.contrib.auth.decorators import login_required
from accounts.models import student_registration #type:ignore
from .models import AttendanceYear,AttendanceMonth
# Create your views here.

Store_some_credential={}

@login_required(login_url='loginAdmin')
def attendanceManager(request):
    if request.method=='POST':
        course=request.POST.get('class')
        semester=request.POST.get('sem')
        try:
            students=get_list_or_404(student_registration,course=course,semester=semester)
            studentData=[
                {
                    "first_name":student.user.first_name,
                    "last_name":student.user.last_name,
                    "rollnumber":student.rollnumber,
                    "enrollment":student.enrollment,
                }
                for student in students
            ]
            context={
                "students":studentData,
            }
            Store_some_credential["students"]=studentData
            return render (request,"attendanceAdd_Update.html",context)
        except Exception as e:
            print(f'Exception of attendanceManager: {e}')
    return render (request,"attendance_manage_admin.html")

@login_required(login_url="loginAdmin")
def saveStudentAttendance(request):
    if request.method == 'POST':
        rollnumber = request.POST.get('rollnumber')
        attendance = request.POST.get('attendance')
        month_input = request.POST.get('month')

        try:
            if month_input:
                year, month = map(int, month_input.split('-'))  # Ensure these are integers
            user = get_object_or_404(student_registration, rollnumber=rollnumber)
            Attendance_Year, created_year = AttendanceYear.objects.get_or_create(
                user=user,
                year=year,
            )
            Attendance_Month, created_month = AttendanceMonth.objects.get_or_create(
                attendance_year=Attendance_Year,
                month=month,
                defaults={'present_days': attendance}
            )

            if not created_month:
                Attendance_Month.present_days = attendance
                Attendance_Month.save()

            print(f'Successfully saved: Year: {year}, Month: {month}, Attendance: {attendance}, User: {user}')
            return render(request, "attendanceAdd_Update.html", {'students': Store_some_credential['students']})
        except Exception as e:
            print(f'Exception in saveStudentAttendance: {e}')

    return redirect('attendanceHome')

@login_required(login_url='loginAdmin')
def showStudentAttendanceStatus(request):
    context={}
    try:
        rollnumber = request.GET.get('rollnumber')
        student = get_object_or_404(student_registration, rollnumber=rollnumber)

        context = {
            "FullName": student.user.first_name + " " + student.user.last_name,
            "Rollnumber": rollnumber,
            "Class": student.course,
            "Semester": student.semester,
        }
        attendance_Y = get_list_or_404(AttendanceYear, user=student)
        
        attendance = []
        for attendance_y in attendance_Y:
            attendance_M = get_list_or_404(AttendanceMonth, attendance_year=attendance_y)
            months = []
            for attendance_m in attendance_M:
                months.append({
                    "month_name": attendance_m.get_month_display(), 
                    "attendance_details": f"{attendance_m.present_days} days",
                })
            attendance.append({
                "year": attendance_y.year,
                "month": months,
            })
        context["Attendance"]=attendance  
          
    except Exception as e:
        print(f"Exception occurred from showStudentAttendanceStatus: {e}")
    return render(request, "showStudentAttendanceStatus.html", context)
    
@login_required(login_url='login')
def student_ShowAttendanceStatus(request):
    context={}
    try:
        rollnumber = request.GET.get('rollnumber')
        student = get_object_or_404(student_registration, rollnumber=rollnumber)

        context = {
            "FullName": student.user.first_name + " " + student.user.last_name,
            "Rollnumber": rollnumber,
            "Class": student.course,
            "Semester": student.semester,
        }
        attendance_Y = get_list_or_404(AttendanceYear, user=student)
        
        attendance = []
        for attendance_y in attendance_Y:
            attendance_M = get_list_or_404(AttendanceMonth, attendance_year=attendance_y)
            months = []
            for attendance_m in attendance_M:
                months.append({
                    "month_name": attendance_m.get_month_display(), 
                    "attendance_details": f"{attendance_m.present_days} days",
                })
            attendance.append({
                "year": attendance_y.year,
                "month": months,
            })
        context["Attendance"]=attendance  
          
    except Exception as e:
        print(f"Exception occurred from showStudentAttendanceStatus: {e}")
    return render(request, "student_ShowAttendanceStatus.html", context)



        
                
    