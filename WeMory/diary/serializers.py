from rest_framework import serializers
from post.serializers import PostSerializer
from .models import Diary
from django.core.serializers import serialize

class DiarySerializer(serializers.ModelSerializer):
    post_list = PostSerializer(many=True, read_only=True)

    class Meta:
        model = Diary
        fields = ('id', 'created_at' , 'updated_at', 'user', 'account_num', 'bank', 'money',
                    'image', 'title', 'goal', 'post_list')
