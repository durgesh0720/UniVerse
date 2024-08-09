from django.shortcuts import render
from adminPannel.models import admin_registration # type: ignore
from django.shortcuts import redirect,get_object_or_404,get_list_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from accounts.models import student_registration #type: ignore
from .models import AssignmentDetails,UserSubmission,UserDetails
from django.utils import timezone
from django.http import JsonResponse

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
            className=request.POST.get('course')
            submission_date=request.POST.get('submission_date')
            questions=request.POST.get('questions')
            unit_number=request.POST.get('unit_number')
            subjectName=request.POST.get('SubjectName')
            semester = request.POST.get('sem')

            user_full_name=admin_user.user.first_name+' '+"sir"
            assignments=AssignmentDetails(
                assignment_number=assignment_number,
                unit_title=title,
                className=className,
                due_date=submission_date,
                questions=questions,
                submit_by=user_full_name,
                unit_number=unit_number,
                subject_name=subjectName,
                semester=semester,
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
    try:
        assignment_id=request.GET.get('id')
        print(f'Edit assignment id: {assignment_id}')
        assignment=get_object_or_404(AssignmentDetails,id=assignment_id)
        admin = assignment.admin_user.user
        username = admin.username
        print(f"Assignment: {assignment}")
        return render(request,"edit_assignment.html",{'assignment':assignment,'username':username})
    except Exception as e:
        print(f'Exception of Edit Assignment: {e}')

login_required(login_url='loginAdmin')
def updateAssignment(request):
    url_id = 0
    if request.method == "POST":
        assignment_id = request.POST.get('assignmentid')
        print("Assignment ID: ",assignment_id)
        if assignment_id:
            url_id = assignment_id
            try:
                assignment = get_object_or_404(AssignmentDetails, id=assignment_id)
                assignment.assignment_number = request.POST.get('assignment_number')
                assignment.unit_title = request.POST.get('title')
                assignment.className = request.POST.get('course')# In HTML: Course here store in className
                assignment.due_date = request.POST.get('submission_date')
                assignment.questions = request.POST.get('questions')
                assignment.submit_by = request.POST.get('submitted_by')
                assignment.unit_number = request.POST.get('unit_number')
                assignment.subject_name = request.POST.get('subject_name')
                assignment.semester = request.POST.get('semester')
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
        assignment_id=request.GET.get('id')
        return redirect(f'/admin-pannel/edit-assignment/?id={assignment_id}')

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
    
login_required(login_url='login')
def showAssignmentStudent(request):
    eligible = False
    username = request.GET.get('username')
    assignment_status = "You need to attempt"
    admin_message = ""

    try:
        student = get_object_or_404(student_registration, user=get_object_or_404(User, username=username))
        student_course = student.course
        student_sem = student.semester
        assignments = get_list_or_404(AssignmentDetails, className=student_course, semester=student_sem)

        try:
            student_submissions = UserSubmission.objects.filter(user__roll_number=student.rollnumber)
            # Check if any submission is checked and get the admin message if available
            for submission in student_submissions:
                if submission.is_checked:
                    assignment_status = "Assignment accepted"
                    if submission.massage:
                        admin_message = submission.massage
                else:
                    assignment_status = "Assignment pending"
        except Exception as e:
            print(f'Exception of assignmentsSubmissionStatus: {e}')
            assignment_status = "You need to attempt"

        assignment_data = [
            {
                'assignment_number': assignment.assignment_number,
                'unit_title': assignment.unit_title,
                'className': assignment.className,
                'semester': assignment.semester,
                'created_date': assignment.created_date,
                'due_date': assignment.due_date,
                'questions': assignment.questions,
                'submit_by': assignment.submit_by,
                'unit_number': assignment.unit_number,
                'subject_name': assignment.subject_name,
                'id':assignment.id,
            }
            for assignment in assignments
        ]
        
        eligible = True
        context = {
            'assignments': assignment_data,
            'username': username,
            'eligible': eligible,
            'assignmentStatus': assignment_status,
            'massage': admin_message,
        }
        
        return render(request, "show_assignments.html", context)
    except Exception as e:
        print(f'Exception occurred in showAssignmentStudent: {e}')
        context = {
            'eligible': eligible,
            'username': username,
        }
        return render(request, "show_assignments.html", context)
    
def saveStudentAssignment(request):
    if request.method=='POST':
        username=request.POST.get('username')
        assignmentid=request.POST.get('assignment_id')
        assignment_file=request.FILES.get('assignment_file')
        try:
            student=get_object_or_404(student_registration,user=get_object_or_404(User,username=username))
            if assignment_file:
                submissionUser=UserDetails(
                    first_name=student.user.first_name,
                    last_name=student.user.last_name,
                    roll_number=student.rollnumber,
                    _class=student.course,
                    semester=student.semester,
                )
                submissionUser.save()
                assignmentSubmission=UserSubmission(
                    assignment_file=assignment_file,
                    submitted_at=timezone.now(),
                    assignmentid=assignmentid,
                    user=submissionUser,
                )
                assignmentSubmission.save()
            return JsonResponse({'success': True})
        except Exception as e:
            print(f"Exception occured from saveStudentAssignment: {e}")
        return JsonResponse({'success': False, 'error': 'Invalid request'}, status=400)

def showAssignmentSubmissions(request):
    assignmentid=request.GET.get('id')
    checkAssignments=False
    context={}
    try:
        assignmentSubmissions=get_list_or_404(UserSubmission,assignmentid=assignmentid)
        studentSubmissions=[
            {
                "student_name":submission.user.first_name+" "+submission.user.last_name,
                "file":submission.assignment_file,
                "class":submission.user._class,
                "semester":submission.user.semester,
                "submitted_at":submission.submitted_at,
            }
            for submission in assignmentSubmissions
        ]
        context={
            "submissions":studentSubmissions,
            "checkAssignments":checkAssignments,
        }
    except Exception as e:
        print(f'Exception occured from showAssignmentSubmissions {e}')
        checkAssignments=True
    return render(request,"showStudentSubmission.html",context)









