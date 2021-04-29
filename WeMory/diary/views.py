from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import DiarySerializer
from .models import Diary
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

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

