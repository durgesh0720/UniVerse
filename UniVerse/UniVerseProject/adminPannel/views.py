from django.shortcuts import render
from .models import admin_registration
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from assignments_manager import views #type: ignore
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def signupAdmin(request):
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']='Username already exist'
        if request.GET['error']==str(2):
            d1['errmsg']='Password & Confirm Password does not match'
    except:
        d1['errmsg']=''
    return render(request,"signupAdmin.html")

def loginAdmin(request):
    if request.user.is_authenticated:
        return redirect(f'/admin-pannel/admin-pannel/?username={request.user.username}')
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']='You have entered an invalid ID number or username and password'
        if request.GET['error']==str(2):
            d1['errmsg']='Wrong credentials'
    except:
        d1['errmsg']=''
    return render(request,"loginAdmin.html",d1)

login_required(login_url="loginAdmin")
def adminPage(request):
    username=request.GET['username']
    try:
        admin=User.objects.filter(username=username).first()
        print(f"adminPage: {admin}")
        if admin:
            context={
                    'firstname':admin.first_name,
                    'lastname':admin.last_name,
                    'username':admin.username,
                    }
            return render(request,"adminPage.html",context)
        else:
            return redirect("loginAdmin")
    except Exception as e:
        print(f"Exception of admin Page: {e}")

def save_admin(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        id=request.POST['id_number']
        password=request.POST['password']
        username=request.POST['username']
        reEnteredPassword=request.POST['re_enter_password']
        try:
            if not password == reEnteredPassword:
                return redirect('/admin-pannel/signup-admin?error=2')
            
            check_username_exists=User.objects.filter(username=request.POST['username'])
            if not check_username_exists:
                user=User.objects.create(
                        first_name=firstname,
                        last_name=lastname,
                        email=email,
                        username=username,
                    )
                user.set_password(password)
                print(f"User: {user}")
                user.save()
                admin_ = admin_registration(
                    user=user,
                    mobile=mobile,
                    id_number=id,
                )
                admin_.save()
                login(request,user)
                return redirect(f'/admin-pannel/admin-pannel/?username={username}')
            else:
                return redirect('/admin-pannel/signup?error=1')
        except Exception as e:
            print(f"Exception: {e}")
    else:
        return redirect('signup-admin')

def Admin_login(request):
    if request.method=='POST':
        id=request.POST['id_number']
        username=request.POST['username']
        password=request.POST['password']
        try:
            if username:
                admin_user=authenticate(username=username,password=password)
                print(f"admin_user: {admin_user}")
                if admin_user is None:
                    return redirect('/admin-pannel/loginAdmin?error=1')
                else:
                    login(request, admin_user)
                    return redirect(f'/admin-pannel/admin-pannel/?username={username}')
            elif id:
                admin=admin_registration.objects.filter(id_number=id).first()
                if admin:   
                    admin_user=admin.user
                    is_valid=authenticate(username=admin_user.username,password=password)
                    print(f"is_valid:{is_valid}")
                    if is_valid is None:
                        return redirect('/admin-pannel/loginAdmin?error=1')
                    else:
                        login(request, is_valid)
                        return redirect(f'/admin-pannel/admin-pannel/?username={admin_user.username}')
            else:
                return redirect('/admin-pannel/loginAdmin?error=1')  
        except Exception as e:
            print(f"Exception: {e}")
            return redirect('/admin-pannel/loginAdmin?error=1')  
    else:
        return redirect('loginAdmin')

def sign_out(request):
    logout(request)
    return redirect('admin-home')
    


