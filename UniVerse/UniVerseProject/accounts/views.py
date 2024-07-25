from django.shortcuts import render
from .models import student_registration
from django.shortcuts import redirect,get_object_or_404
from django.http import HttpResponse
# from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

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
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']="Username and password dosen't matched "
    except:
        d1['errmsg']=""
    return render(request,"login.html",d1)

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
                context = {
                    'firstname': request.POST['firstname'],
                    'lastname': request.POST['lastname'],
                    'username': request.POST['username']
                }
                return render(request, "Welcome.html", context)
            else:
                url = "http://localhost:8000/signup?error=1"
                return redirect(url)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
        print(f"An error occurred: {e}")
        return redirect('home')
    
def checkUser(request):
    try:
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return redirect('/login?error=1')
        else:
            login(request, user)
            context = {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'username': user.username,
            }
            return render(request, "Welcome.html", context)
    except Exception as e:
        print(f"Error during authentication: {e}")
        return redirect('/login?error=1')

def profile(request):
        username = request.GET['username']
        user = get_object_or_404(User, username=username)
        student = get_object_or_404(student_registration, user=user)
        return render(request, "profile.html", {"user": user, "student": student})

def update_profile(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            mobile = request.POST['mobile']
            email = request.POST['email']
            admission_year = request.POST['admission_year']
            rollnumber = request.POST['rollnumber']
            enrollment = request.POST['enrollment']
            profile_picture = request.FILES.get('profile_picture')
            course = request.POST.get('course')

            print("Received POST data:")
            print(f"username: {username}, firstname: {firstname}, lastname: {lastname}")
            print(f"mobile: {mobile}, email: {email}, admission_year: {admission_year}")
            print(f"rollnumber: {rollnumber}, enrollment: {enrollment}")
            print(f"profile_picture: {profile_picture}, course: {course}")

            user = get_object_or_404(User, username=username)
            print(f"User found: {user}")
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
            student.admission_year = admission_year
            if profile_picture:
                student.profile_picture = profile_picture
            student.save()

            context = {
                'firstname': user.first_name,
                'lastname': user.last_name,
                'username': user.username,
            }
            return render(request, "Welcome.html", context)
        except KeyError:
            return HttpResponse("Invalid form data")
        except User.DoesNotExist:
            return HttpResponse("User not found")
        except student_registration.DoesNotExist:
            return HttpResponse("Student registration not found")
    else:
        return redirect("login")
    
def log_out(request):
    logout(request)
    return redirect("home")