from django.urls import path
from . import views


urlpatterns = [
    path('videos/',views.post_videos.as_view(), name="videos-post"), #to get all videos and upload video
    path('delete_video/<int:sno>/',views.delete_yourvideo.as_view(), name="video-delete"), #to delete the video
    path('userdetails/',views.get_user_details.as_view(), name="user-details"), #to get all user details
    path('alluservideos/',views.get_all_user_videos.as_view(), name="users-all-videos"), #to get all videos of user
    path('viewcount/<int:sno>/',views.view_counter.as_view(), name="view-count"), #to count the view of video
    path('increase/like/<int:sno>/',views.IncrementLike.as_view()),
    path('decrease/like/<int:sno>/',views.DecrementLike.as_view()),
    path('createprofile/',views.create_profile.as_view(), name='createprofile'),
    path('updateprofile/',views.update_profile.as_view(), name="update-profile"),
    path('following/', views.FollowingListView.as_view(), name='following-list'),
    path('followers/', views.FollowerListView.as_view(), name='follower-list'),
]