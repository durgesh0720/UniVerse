from django.shortcuts import render
from .models import student_registration
from django.shortcuts import redirect,get_object_or_404,get_list_or_404
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from assignments_manager.models import AssignmentDetails #type: ignore
from attendance_manager.models import AttendanceYear,AttendanceMonth #type: ignore
from datetime import datetime


import logging
logger = logging.getLogger(__name__)

def homepage(request):
    return render(request,"home.html")

@ensure_csrf_cookie
def signup(request):
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']="Username already exists"
    except:
        d1['errmsg']=''
    return render(request,"signup.html",d1)

def log_in(request):
    if request.user.is_authenticated:
        return redirect(f'/welcome/?username={request.user.username}')
    try:
        d1={}
        try:
            if request.GET['error']==str(1):
                d1['errmsg']="Username and password dosen't matched "
        except:
            d1['errmsg']=""
        return render(request,"login.html",d1)
    except Exception as e:
        print(f"Exception of User login: {e}")
        return redirect('login')
    
@login_required(login_url='login')
def welcomepage(request):
    try:
        username=request.GET.get('username')
        user=User.objects.filter(username=username).first()
        context={
            'firstname':user.first_name,
            'lastname':user.last_name,
            'username':user.username,
        }
        return render(request,'Welcome.html',context)
    except Exception as e:
        print(f"Exception in Welcome Page: {e}")
        return redirect('login')

@csrf_protect
def saveUsers(request):
    try:
        if request.method == "POST":
            logger.debug(f"CSRF cookie: {request.COOKIES.get('csrftoken')}")
            logger.debug(f"CSRF token in POST: {request.POST.get('csrfmiddlewaretoken')}")

            check_username_exists=User.objects.filter(username=request.POST['username'])
            if not check_username_exists:
                user=User.objects.create(
                    first_name=request.POST['firstname'],
                    last_name=request.POST['lastname'],
                    email=request.POST['email'],
                    username=request.POST['username'],
                )
                print(f'User:{user}')
                user.set_password(request.POST['password'])
                user.save()
                student=student_registration(
                    user=user,
                )
                student.save()   
                print(f'student:{student}')         
                username=user.username
                return redirect(f'/welcome/?username={username}')
            else:
                url = "http://localhost:8000/signup?error=1"
                return redirect(url)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return redirect('home')
    
def checkUser(request):
    try:
        if request.method=='POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(username=username, password=password)
            
            if user is None:
                return redirect('/login?error=1')
            else:
                login(request, user)
                return redirect(f'/welcome/?username={username}')
        else:
            return redirect('/login?error=1')
    except Exception as e:
        print(f"Error during authentication: {e}")
        return redirect('/login?error=1')

@login_required(login_url='login')
def profile(request):
    try:
        username = request.GET['username']
        user = get_object_or_404(User, username=username)
        student = get_object_or_404(student_registration, user=user)
        return render(request, "profile.html", {"user": user, "student": student})
    except Exception as e:
        print(f'Exception occured from Account/profile {e}')
        return redirect('login')
    
@login_required(login_url='login')
def edit_profile(request):
    try:
        print(request)
        username = request.GET['username']
        user = get_object_or_404(User, username=username)
        student = get_object_or_404(student_registration, user=user)
        return render(request, "edit_profile.html", {"user": user, "student": student})
    except Exception as e:
        print(f"Exception: {e}")
        return redirect('login')

@login_required(login_url='login')
def update_profile(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            mobile = request.POST['mobile']
            email = request.POST['email']
            sem = request.POST['sem']
            rollnumber = request.POST['rollnumber']
            enrollment = request.POST['enrollment']
            profile_picture = request.FILES.get('profile_picture')
            course = request.POST.get('course')
            address = request.POST['address']
            bio = request.POST['bio']
            profession = request.POST['profession']
            dob=request.POST['dob']
            # print(f"profile_picture: {profile_picture}, course: {course}")

            user = get_object_or_404(User, username=username)
            print(f"User found: {user}")
            print(f'Profile_picture: {profile_picture}')
            student = get_object_or_404(student_registration, user=user)
            print(f"Student registration found: {student}")

            user.first_name = firstname
            user.last_name = lastname
            user.email = email
            user.save()

            student.rollnumber = rollnumber
            student.enrollment = enrollment
            student.course = course
            student.mobile = mobile
            student.semester = sem
            student.bio=bio
            student.dob=dob
            student.address=address
            student.profession=profession
            if profile_picture:
                student.profile_picture = profile_picture
            student.save()

            context = {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'username': user.username,
            }
            return render(request, "Welcome.html", context)
        except KeyError as e:
            print(f"Invalid form data{e}")
            return HttpResponse("Invalid form data=",e)
        except User.DoesNotExist:
            return HttpResponse("User not found")
        except student_registration.DoesNotExist:
            return HttpResponse("Student registration not found")
    else:
        return redirect("login")
    
def log_out(request):
    logout(request)
    return redirect("home")

login_required(login_url='login')
def dashboard(request):
    context={
        "error":"Not found data"
    }
    username=request.GET.get("username")
    try:
        user=User.objects.filter(username=username).first()
        print(f'user: {user}')
        student=get_object_or_404(student_registration,user=user)
        print(f'Student: {student}')
        context["student"]=student
        course=student.course
        semester=student.semester
        assignments=get_list_or_404(AssignmentDetails,className=course,semester=semester)
        AssignmentData=[
            {
                "due_date":assignment.due_date,
                "unit_title":assignment.unit_title,
            }
            for assignment in assignments
        ]
        context["assignments"]=AssignmentData

        current_year = datetime.now().year
        attendance_y = get_list_or_404(AttendanceYear, user=student, year=current_year)
        attendance = []
        for attendance_y in attendance_y:
            attendance_m = get_list_or_404(AttendanceMonth, attendance_year=attendance_y)
            months = []
            for attendance_m in attendance_m:
                months.append({
                    "month_name": attendance_m.get_month_display(), 
                    "attendance_details": f"{attendance_m.present_days} days",
                })
            attendance.append({
                "year": attendance_y.year,
                "month": months,
            })
        context["attendances"] = attendance
        context['error']=""
        return render(request,"dashboard.html",context)
    except Exception as e:
        print(f'Exception of student dashboard : {e}')
        context['error']=f"{e}"
        return render(request,"dashboard.html",context)