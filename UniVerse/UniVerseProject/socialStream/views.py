from django.shortcuts import render
from accounts.models import student_registration
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import post,Comment,Like

# Create your views here.
@login_required
def feedpage(request):
    user = request.user
    posts_data = []
    comments=None
    student = student_registration.objects.filter(user=user).first()
    try:
        posts = post.objects.all().order_by('-timestamp')
        posts_data = []
        for Post in posts:
            user_profile = student_registration.objects.filter(user=Post.user).first()
            post_data = {
                'username': Post.user.username,  # Adjusted if needed
                'text': Post.content,
                'timestamp': Post.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'id':Post.id,
                'profile': user_profile.profile_picture if user_profile and user_profile.profile_picture else None
            }
            try:
                comments=Comment.objects.filter(post=Post)
                post_data['comments']=comments
            except:
                post_data['comments']=comments
            if post.file:
                post_data['file']=Post.file
            posts_data.append(post_data)
            
    except Exception as e:
        print(f"Error: {e}")
        posts_data = [f"Error: {e}"]
    
    context = {
        'name':user.first_name,
        'username':user.username,
        'posts': posts_data,
        'currunt_user_profile': student.profile_picture if student and student.profile_picture else None,
    }
    return render(request, "socialStream/feedpage.html", context)
