from django.shortcuts import render
from adminPannel.models import admin_registration # type: ignore
from django.shortcuts import redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import AssignmentDetails
from django.utils import timezone

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
            return render(request,"Assignment_manager_home.html",{"username":username,"firstname":admin.first_name,"lastname":admin.last_name})
    except Exception as e:
        print(f"Ecxeption: {e}")
        return redirect('/admin-pannel/loginAdmin?error=2')
    
login_required(login_url='loginAdmin')
def upload_assignment(request):
    username = request.GET.get('username')
    admin=User.objects.filter(username=username).first()
    if admin is None:
            return redirect('/admin-pannel/loginAdmin?error=2')
    else:
         admin_user=admin_registration.objects.filter(user=admin).first()
         print(f"Admin_User:{admin_user}")
         assignments = AssignmentDetails.objects.filter(admin_user=admin_user)
         print(f"Assignments: {assignments}")
         context={
              "assignments":assignments,
              "id_number":admin_user.id_number,
         }
         return render(request,"upload_assignment.html",context)


login_required(login_url='loginAdmin')
def saveAssignments(request):
    if request.method=="POST":
        id=request.GET.get('id')
        admin_user=admin_registration.objects.filter(id_number=id).first()
        if admin_user is None:
            print(f"Admin_user: {admin_user}")
            return redirect('/admin-pannel/loginAdmin?error=2')
        else:
            assignment_number=request.POST.get('assignment_number')
            title=request.POST.get('title')
            className=request.POST.get('class')
            submission_date=request.POST.get('submission_date')
            questions=request.POST.get('questions')
            unit_number=request.POST.get('unit_number')
            user_full_name=admin_user.user.first_name+' '+"sir"
            assignments=AssignmentDetails(
                assignment_number=assignment_number,
                unit_title=title,
                className=className,
                due_date=submission_date,
                questions=questions,
                submit_by=user_full_name,
                unit_number=unit_number,
                is_checked=False,
                created_date=timezone.now(),
                admin_user=admin_user,
            )
            assignments.save()

            user=admin_user.user
            username=user.username
            return redirect(f'/admin-pannel/upload-assignment/?username={username}')        
    else:
        return redirect('upload-assignment')

login_required(login_url="loginAdmin")
def editAssignment(request):
    id=request.GET.get('id')
    assignment=get_object_or_404(AssignmentDetails,id=id)
    print(f"Assignment: {assignment}")
    return render(request,"edit_assignment.html",{'assignment':assignment})

login_required(login_url='loginAdmin')
def updateAssignment(request):
    url_id = 0
    if request.method == "POST":
        assignment_id = request.POST.get('assignmentid')
        if assignment_id:
            url_id = assignment_id
            print('Entered')
            try:
                assignment = get_object_or_404(AssignmentDetails, id=assignment_id)
                assignment.assignment_number = request.POST.get('assignment_number')
                assignment.unit_title = request.POST.get('title')
                assignment.className = request.POST.get('class')
                assignment.due_date = request.POST.get('submission_date')
                assignment.questions = request.POST.get('questions')
                assignment.submit_by = request.POST.get('submitted_by')
                assignment.unit_number = request.POST.get('unit_number')
                assignment.save()
                admin = assignment.admin_user.user
                username = admin.username
                return redirect(f"/admin-pannel/upload-assignment?username={username}")
            except Exception as e:
                print(f'Exception of Update Assignment: {e}')
                return redirect(f'/admin-pannel/edit-assignment/?id={url_id}')
        else:
            print('Assignment ID is missing in the POST data.')
            return redirect(f'/admin-pannel/edit-assignment/?id={url_id}')
    else:
        return redirect(f'/admin-pannel/edit-assignment/?id={url_id}')

login_required(login_url="loginAdmin")
def deleteAssignment(request):
    id=request.GET.get('id')
    try:
        assignment=get_object_or_404(AssignmentDetails,id=id)
        admin = assignment.admin_user.user
        username = admin.username
        assignment.delete()
        return redirect(f"/admin-pannel/upload-assignment?username={username}")
    except Exception as e:
        print(f'Exception of Update Assignment: {e}')
        return redirect(f'/admin-pannel/edit-assignment/?id={id}')





