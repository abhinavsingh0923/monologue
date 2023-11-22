from rest_framework.decorators import APIView
from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *

# Create your views here.

class create_profile(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data=request.data
        user_id = request.user.id
        email_id = request.user.email
        data.update({"user":user_id,"email": email_id})
        serializer=createProfileSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status":status.HTTP_202_ACCEPTED,"data":serializer.data})
        return Response({"status":status.HTTP_400_BAD_REQUEST, 'error':serializer.errors})

class update_profile(APIView):
    permission_classes=[IsAuthenticated]
    def patch(self, request):
        serializer=createProfileSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED,msg='updates')
        return Response({"status":status.HTTP_400_BAD_REQUEST, 'error':serializer.errors})

class post_videos(APIView):
    permission_classes = [IsAuthenticated]
    # to get all reals
    def get(self,request):
        post_obj= post.objects.all().order_by('?')[:50]
        serializer = postserializer(post_obj, many=True)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    # to post the reels 
    def post(self,request):
        try:
            data=request.data
            user_id = request.user.id
            # Adding user_id to the data dictionary
            data.update({"user":user_id})
            serializer=postserializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_201_CREATED,msg='blog is successfully created',data=serializer.data)
        except Exception as e:    
            return Response({"status":status.HTTP_400_BAD_REQUEST, 'error':e}) 
          

# to delete your reel         
class delete_yourvideo(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,sno):
        post_delete=post.objects.get(pk=sno)
        post_delete.delete()
        return Response(status=status.HTTP_404_NOT_FOUND,msg="sucessfully reel is delete")
    
    def get(self,request,sno):
        get_post=post.objects.get(pk=sno)
        serializer = postserializer(get_post)
        return Response(status=status.HTTP_200_OK,msg='sucessfully loaded',data=serializer.data)
    
# to get user details
class get_user_details(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user_obj=profile.objects.get(user=request.user)
        serializer=profileserializer(user_obj)
        following_count = request.user.following.count()
        follower_count = request.user.followers.count()
        return Response(data={'data':serializer.data,"following":following_count,"follower":follower_count}, status=status.HTTP_200_OK)    

# to user all reels
class get_all_user_videos(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        post_obj=post.objects.filter(user=request.user)
        serializer=postserializer(post_obj,many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK,msg="all user videos has been send to client successfully")
    
# to count view 
class view_counter(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,sno):
        video = post.objects.get(pk=sno)
        video.no_of_views += 1 
        video.save()
        serializer = postserializer(video)
        return Response(status=status.HTTP_200_OK,data=serializer.data)
    
# to count like 
class IncrementLike(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, sno):
        try:
            video = post.objects.get(pk=sno)
            video.no_of_likes += 1
            video.save()
            serializer = postserializer(video)
            return Response(status=status.HTTP_200_OK,data=serializer.data)
        except post.DoesNotExist:
            return Response({"status":status.HTTP_400_BAD_REQUEST, 'error':serializer.errors})

class DecrementLike(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request, sno):
        try:
            video = post.objects.get(pk=sno)
            if video.no_of_likes > 0:
                video.no_of_likes -= 1
                video.save()
                serializer = postserializer(video)
                return Response(status=status.HTTP_200_OK,data=serializer.data)
            else:
                return Response(status= status.HTTP_400_BAD_REQUEST,msg= "Number of likes is already zero")
        except post.DoesNotExist:
            return Response({"status":status.HTTP_400_BAD_REQUEST, 'error':serializer.errors})


class FollowCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = profile.objects.get(id=user_id)
        except profile.DoesNotExist:
            return Response({"detail": "User not found."}, status=status.HTTP_404_NOT_FOUND)

        if user_to_follow == request.user:
            return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)

        follow, created = Follow.objects.get_or_create(follower=request.user, following=user_to_follow)
        if created:
            return Response({"detail": "You are now following this user."}, status=status.HTTP_201_CREATED)
        else:
            return Response({"detail": "You are already following this user."}, status=status.HTTP_200_OK)

class UnfollowDestroyView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, follow_id):
        try:
            follow = Follow.objects.get(id=follow_id)
        except Follow.DoesNotExist:
            return Response({"detail": "Follow relationship not found."}, status=status.HTTP_404_NOT_FOUND)

        if follow.follower == request.user:
            follow.delete()
            return Response({"detail": "You have unfollowed this user."}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"detail": "You are not authorized to unfollow this user."}, status=status.HTTP_403_FORBIDDEN)
        
class FollowerListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        followers = request.user.followers.all()
        serializer = profileserializer(followers, many=True)
        return Response(serializer.data)

class FollowingListView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        following = request.user.following.all()
        serializer = profileserializer(following, many=True)
        return Response(serializer.data)