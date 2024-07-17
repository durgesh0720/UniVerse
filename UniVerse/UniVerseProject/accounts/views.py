from django.shortcuts import render
from .models import student_registration
from django.shortcuts import redirect
from django.views.decorators.csrf import requires_csrf_token
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
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

def login(request):
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
        if request.method=="POST":
            logger.debug(f"CSRF cookie: {request.COOKIES.get('csrftoken')}")
            logger.debug(f"CSRF token in POST: {request.POST.get('csrfmiddlewaretoken')}")

            user=student_registration()
            check_username_exists=student_registration.objects.filter(username=request.POST['username'])
            if not check_username_exists:
                user.firstname=request.POST['firstname']
                user.lastname=request.POST['lastname']
                user.email=request.POST['email']
                user.username=request.POST['username']
                user.password=request.POST['password']
                user.save()
                context={
                    'firstname':request.POST['firstname'],
                    'lastname':request.POST['lastname'],
                }
                return render(request,"Welcome.html",context)
            else:
                url="http://localhost:8000/signup?error=1"
            return redirect(url)
    except:
        return redirect('homepage')

def checkUser(request):
    try:
        username=request.POST['username']
        password=request.POST['password']
        is_student=student_registration.objects.filter(username=username,password=password)
        if not is_student.exists():
            url = "http://localhost:8000/login?error=1"
            return redirect(url)
        else:
            student = is_student.values().first()
            context = {
                'firstname': student['firstname'],
                'lastname': student['lastname'],
            }
            return render(request,"Welcome.html",context) 
    except:
        url="http://localhost:8000/login?error=1"
        return redirect(url)