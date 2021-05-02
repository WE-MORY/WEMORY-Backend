from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiarySerializer, DiaryMoneySerializer, GoalSerializer
from .models import Diary, Goal
from post.models import Post
from post.serializers import PostSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status, viewsets
from django_filters.rest_framework import DjangoFilterBackend, filters

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
        diary_serializer = DiaryMoneySerializer(diary) 
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
def goal_list(request):
    if request.method == "POST":
        goal_serializers=GoalSerializer(data=request.data)
        if goal_serializers.is_valid(raise_exception=True):
            goal_serializers.save()
            return Response(goal_serializers.data)
    else:
        goals = Goal.objects.all()
        goal_serializers = GoalSerializer(goals, many=True)
        return Response(goal_serializers.data)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'created_at', 'title', 'received_money')
    http_method_names = ['get']
 

    def get_queryset(self):
        orderbyList = ['created_at']
        q = self.request.GET.get('q')
        date = self.request.GET.get('date')
        month = self.request.GET.get('month')
        
        if q :
            if month:
                return Post.objects.filter(created_at__month__gte=month, diary=q).order_by(*orderbyList)
            elif date:
                return Post.objects.filter(created_at=date, diary=q).order_by(*orderbyList)
            else:
                return Post.objects.filter(diary=q).order_by(*orderbyList)
        else:
            return Post.objects.all().order_by(*orderbyList)