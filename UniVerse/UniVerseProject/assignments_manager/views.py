from django.shortcuts import render
from adminPannel.models import admin_registration # type: ignore
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.

login_required(login_url='loginAdmin')
def assignment_home(request):
    try:
        username = request.GET.get('username')
        admin=User.objects.filter(username=username).first()

        print(f"admin: {admin}")
        print(f"Request:{request} and username: {username}")
        if admin is None:
            return redirect('/admin-pannel/loginAdmin?error=1')
        else:
            print("context")
            # context={
            #     'firstname':admin.first_name,
            #     'lastname':admin.last_name,
            # }
            print("after context")
            return render(request,"Assignment_manager_home.html",{"username":username,"firstname":admin.first_name,"lastname":admin.last_name})
    except Exception as e:
        print(f"Ecxeption: {e}")
        return redirect('/admin-pannel/loginAdmin?error=2')
    
def upload_assignment(request):
    return render(request,"upload_assignment.html")