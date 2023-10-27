from django.db import models
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.
class profile(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_username = models.CharField(unique=True,max_length=50)
    name = models.CharField( max_length=50)
    email = models.EmailField(unique=True, max_length=254)
    bio = models.TextField()
    profile_photo = models.ImageField( upload_to='profile_images', default="profile_img.jpg")
    follows = models.ManyToManyField("profile", related_name="followed_by")


    def __str__(self):
        return self.id_username

class Follow(models.Model):
    follower = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='following')
    following = models.ForeignKey(profile, on_delete=models.CASCADE, related_name='followers')
    created_at = models.DateTimeField(auto_now_add=True)


     
    
class post(models.Model):
    id=models.AutoField(primary_key=True)
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    video=models.FileField( upload_to='post_videos')
    caption=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    no_of_likes=models.IntegerField(default=0)
    no_of_views=models.IntegerField(default=0)
    

    def __str__(self):
        return self.user
    

class todaymonologue(models.Model):
    id = models.AutoField(primary_key=True)
    theme = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    dialogue = models.TextField(max_length=500)
