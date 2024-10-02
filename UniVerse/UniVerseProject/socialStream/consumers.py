from channels.generic.websocket import AsyncWebsocketConsumer
from django.contrib.auth.models import User
from .models import post,Comment,Like  
import json
from datetime import datetime
from accounts.models import student_registration
from channels.db import database_sync_to_async
from asgiref.sync import sync_to_async

class Socialfeeds(AsyncWebsocketConsumer):
    async def connect(self):
        self.user = self.scope.get('user')
        if self.user.is_authenticated:
            print(f"Now User is {self.user} and username is {self.user.username}")
            await self.accept()  # Await accept()

        else:
            await self.close()  # Await close()
    
    async def disconnect(self, close_code):
        print(f"User disconnected with code {close_code}")

    async def receive(self, text_data):
        try:
            text_data_json = json.loads(text_data)
            message = text_data_json.get("message", "")
            file = text_data_json.get('file', None)
            comment=text_data_json.get("comment","")
            like=text_data_json.get("like","")

            if comment:
                print(f"comment recieved: {comment['text']} Id:{comment['postId']}")
                await self.commentSave(comment)
            if message:
                await self.save_post(message, file)
                print(f"Message from client: {message}")

            if like:
                await self.likeSave(like)
                print(f" Like at {like} This post. User {self.user}")

        except json.JSONDecodeError:
            await self.send(text_data=json.dumps({
                "error": "Invalid JSON format",
            }))

    async def save_post(self, content, file):
        post_instance = post(
            user=self.user, 
            content=content, 
            file=file,
            timestamp=datetime.now(),
        )
        await database_sync_to_async(post_instance.save)()  # Async save
        await self.send_post(content, file)
    
    async def send_post(self, content, file):
        picture_user = await database_sync_to_async(
            lambda: student_registration.objects.filter(user=self.user).first()
        )()
        
        post_data = {
            'username': self.user.username,
            'content': content,
            'file': file,
            'timestamp': datetime.now().isoformat(),
            'profile': picture_user.profile_picture.url if picture_user and picture_user.profile_picture else None,
        }
        await self.send(text_data=json.dumps({
            'posts': post_data
        }))

    async def commentSave(self,comment):
        try:
            InstanceOfPost = await sync_to_async(lambda: post.objects.filter(id=comment['postId']).first())()
            if InstanceOfPost:
                InstanceComment=Comment(
                        user=self.user,
                        post=InstanceOfPost,
                        content=comment['text'],
                        timestamp=datetime.now,
                    )
                await sync_to_async(InstanceComment.save)()
        except Exception as e:
            print(f"Exception occured from save comment: {e}")

    async def likeSave(self, postId):
        posts = {}
        try:
            post_instance = await database_sync_to_async(post.objects.filter(id=postId).first)()
            if post_instance:
                existing_like = await database_sync_to_async(Like.objects.filter(user=self.user, post=post_instance).first)()

                if existing_like:
                    print(f"User {self.user} has already liked post {postId}")
                    await database_sync_to_async(existing_like.delete)()
                    posts['likeStatus'] = "Like"

                else:
                    like_instance = Like(
                        user=self.user,
                        post=post_instance,
                        timestamp=datetime.now(),  
                    )
                    print("Saving like for post ID:", postId)
                    await database_sync_to_async(like_instance.save)()
                    posts['likeStatus'] = "Liked"
                
                posts['postId'] = postId
            
            like_count = await database_sync_to_async(Like.objects.filter(id=postId).count)()
            posts['likeCount'] = like_count
            await self.send(text_data=json.dumps({
                'likeStatus': posts
            }))
            
        except Exception as e:
            print(f"Exception occurred while saving like: {e}")

    
    def follow(self):
        posts={}
        

