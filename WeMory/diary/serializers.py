from rest_framework import serializers
from post.serializers import PostSerializer
from .models import Diary, Goal
from post.models import Post
from django.core.serializers import serialize


class GoalSerializer(serializers.ModelSerializer):

    class Meta:
        model = Goal
        fields = ('goal', 'goal_title', 'goal_diary')


class DiarySerializer(serializers.ModelSerializer):
    post_list = PostSerializer(many=True, read_only=True)
    goal_list = GoalSerializer(many=True, read_only=True)
    class Meta:
        model = Diary
        fields = ('id', 'created_at' , 'updated_at', 'user', 'account_num', 'bank', 'money',
                    'image', 'title', 'post_list', 'goal_list')


class DiaryMoneySerializer(serializers.ModelSerializer):
    sum_money = serializers.SerializerMethodField()
    post_list = PostSerializer(many=True, read_only=True)
    goal_list = GoalSerializer(many=True, read_only=True)
    class Meta:
        model = Diary
        fields = ('id', 'created_at' , 'updated_at', 'user', 'account_num', 'bank', 'money',
                    'image', 'title', 'sum_money', 'post_list', 'goal_list')
    
    def get_sum_money(self, obj):
        money_list = Post.objects.filter(diary=obj.id).values_list('received_money')
        return money_list


class UserDiarySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Diary
        fields = ('id', 'account_num', 'bank','image', 'title')


