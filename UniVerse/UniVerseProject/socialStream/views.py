from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import post, Comment, Like
from accounts.models import student_registration

@login_required
def feedpage(request):
    user = request.user
    posts_data = []

    try:
        student = student_registration.objects.filter(user=user).first()
        posts = post.objects.all().order_by('-timestamp').select_related('user')

        for Post in posts:
            user_profile = student_registration.objects.filter(user=Post.user).first()
            
            comments = Comment.objects.filter(post=Post)
            like_count = Like.objects.filter(post=Post).count()
            comments_count = Comment.objects.filter(post=Post).count()

            user_likes_post = Like.objects.filter(post=Post, user=user).exists()
            is_like = "Unlike" if user_likes_post else "Like"

            post_data = {
                'username': Post.user.username,
                'text': Post.content,
                'timestamp': Post.timestamp.strftime('%Y-%m-%d %H:%M:%S'),
                'id': Post.id,
                'profile': user_profile.profile_picture if user_profile and user_profile.profile_picture else None,
                'comments': comments,
                'likes': like_count,
                'commentCount':comments_count,
                'likeStatus': is_like, 
            }
            
            if Post.file:
                post_data['file'] = Post.file
            
            posts_data.append(post_data)

    except Exception as e:
        print(f"Error: {e}")
        posts_data = [{"error": "An error occurred while fetching posts."}]
    

    context = {
        'name': user.first_name,
        'username': user.username,
        'posts': posts_data,
        'currunt_user_profile': student.profile_picture if student and student.profile_picture else None,
    }
    
    return render(request, "socialStream/feedpage.html", context)
