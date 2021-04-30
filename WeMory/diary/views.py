from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiarySerializer, PostSerializer
from .models import Diary, Post
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def diary_list(request):
    if request.method == "POST":
        diary_serializers=DiarySerializer(data=request.data)
        if diary_serializers.is_valid(raise_exception=True):
            diary_serializers.save()
            return Response(diary_serializers.data)
    else:
        diaries = Diary.objects.all()
        diary_serializers = DiarySerializer(diaries, many=True)
        return Response(diary_serializers.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def diary_detail(request, pk):
    try: 
        diary = Diary.objects.get(pk=pk) 
    except Diary.DoesNotExist: 
        return JsonResponse({'message': 'The diary does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        diary_serializer = DiarySerializer(diary) 
        return Response(diary_serializer.data) 
 
    elif request.method == 'PUT': 
        diary_data = JSONParser().parse(request) 
        diary_serializer = DiarySerializer(diary, data=diary_data) 
        if diary_serializer.is_valid(): 
            diary_serializer.save() 
            return JsonResponse(diary_serializer.data) 
        return JsonResponse(diary_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        diary.delete() 
        return JsonResponse({'message': 'diary was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def post_list(request):
    if request.method == "POST":
        post_serializers=PostSerializer(data=request.data)
        if post_serializers.is_valid(raise_exception=True):
            post_serializers.save()
            return Response(post_serializers.data)
    else:
        posts = Post.objects.all()
        post_serializers = PostSerializer(posts, many=True)
        return Response(post_serializers.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def post_detail(request, pk):
    try: 
        post = Post.objects.get(pk=pk) 
    except Post.DoesNotExist: 
        return JsonResponse({'message': 'The post does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        post_serializer = PostSerializer(post) 
        return Response(post_serializer.data) 
 
    elif request.method == 'PUT': 
        post_data = JSONParser().parse(request) 
        post_serializer = PostSerializer(post, data=post_data) 
        if post_serializer.is_valid(): 
            post_serializer.save() 
            return JsonResponse(post_serializer.data) 
        return JsonResponse(post_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        post.delete() 
        return JsonResponse({'message': 'post was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)