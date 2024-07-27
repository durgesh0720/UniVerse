from django.shortcuts import render
from .models import admin_registration
from django.shortcuts import redirect
# Create your views here.

def homepage(request):
    return render(request,"homepage.html")

def signupAdmin(request):
    return render(request,"signupAdmin.html")

def loginAdmin(request):
    d1={}
    try:
        if request.GET['error']==str(1):
            d1['errmsg']='ID number is not correct'
    except:
        d1['errmsg']=''
    return render(request,"loginAdmin.html",d1)

def save_admin(request):
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        mobile=request.POST['mobile']
        id=request.POST['id_number']
        password=request.POST['password']

        if not admin_registration.objects.filter(id_number=id):
            admin=admin_registration.objects.create(
                first_name=firstname,
                last_name=lastname,
                email=email,
                mobile=mobile,
                id_number=id,
                password=password
            )
            admin.save()
            context={
                'firstname':firstname,
                'lastname':lastname,
                'id':id
            }
            return render(request,"adminPage.html",context)
        else:
            return redirect('loginAdmin')
    else:
        return redirect('signup-admin')

def Admin_login(request):
    if request.method=='POST':
        id=request.POST['id_number']
        password=request.POST['password']

        admin=admin_registration.objects.filter(id_number=id,password=password).first()
        
        if admin is None:
            return redirect('/admin-pannel/loginAdmin?error=1')
        else:
            context={
                'firstname':admin.first_name,
                'lastname':admin.last_name,
                'id':admin.id_number
            }
            return render(request,"adminPage.html",context)
    else:
        return redirect('loginAdmin')

def sign_out(request):
    return redirect('admin-home')

    




