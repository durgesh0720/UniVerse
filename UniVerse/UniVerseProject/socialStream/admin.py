from django.contrib import admin
from .models import post,Comment,Like
# Register your models here.
@admin.register(post)
class PostsAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'timestamp')
    search_fields = ('content',)
    list_filter = ('timestamp',)

