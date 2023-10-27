from rest_framework import serializers
from api.models import *

class postserializer(serializers.ModelSerializer):
    class Meta:
            model = post
            fields ='__all__'

class profileserializer(serializers.ModelSerializer):

    class Meta:
            model = profile
            fields ='__all__'

class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follow
        fields = ('id', 'follower', 'following', 'created_at')

class createProfileSerializer(serializers.ModelSerializer):
     class Meta:
          model = profile
          fields = ('user' ,'name' , 'email', 'id_username', 'bio', 'profile_photo')