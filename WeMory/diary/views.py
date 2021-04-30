from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiarySerializer
from .models import Diary
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


@api_view(['GET','POST'])
@permission_classes([AllowAny])
def diary_list(request):
    if request.method == "POST":
        serializers=DiarySerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    else:
        diaries = Diary.objects.all()
        serializers = DiarySerializer(diaries, many=True)
        return Response(serializers.data)

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