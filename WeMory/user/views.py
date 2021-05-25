from rest_framework import status, viewsets, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from .serializers import SignUpSerializer, SignInSerializer, UserSerializer
from .models import User
from account.models import Account

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core import serializers
import requests
import json
import time
import random


from rest_framework_jwt.settings import api_settings
JWT_DECODE_HANDLER = api_settings.JWT_DECODE_HANDLER
JWT_PAYLOAD_GET_USER_ID_HANDLER = api_settings.JWT_PAYLOAD_GET_USER_ID_HANDLER

@api_view(['GET'])
@permission_classes([AllowAny])
def getCellCerti(request):
    if request.method == 'GET':
        CellCerti = random.randint(100000, 999999)
        return Response({"CellCerti": str(CellCerti)}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([AllowAny])
def signUp(request):
    if request.method == 'POST':
        serializer = SignUpSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Body 값이 잘못되었습니다."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['password'] != serializer.validated_data['password_confirm']:
            return Response({"message": "Password가 일치하지 않습니다"}, status=status.HTTP_409_CONFLICT)
        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "중복된 이메일입니다."}, status=status.HTTP_409_CONFLICT)


@api_view(['POST'])
@permission_classes([AllowAny])
def signIn(request):
    if request.method == 'POST':
        serializer = SignInSerializer(data=request.data)

        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "잘못된 Body값입니다."}, status=status.HTTP_409_CONFLICT)
        if serializer.validated_data['email'] == "None":
            return Response({"message": "로그인에 실패하였습니다."}, status=status.HTTP_409_CONFLICT)
        
        response = {
            'success': 'True',
            'token': serializer.data['token']
        }
        return Response(response, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JSONWebTokenAuthentication])
def getUserId(request):
    
    if request.method == 'GET':
        token = request.META.get('HTTP_AUTHORIZATION', " ").split(' ')[1]
        payload = JWT_DECODE_HANDLER(token)
        user_id = JWT_PAYLOAD_GET_USER_ID_HANDLER(payload)

        user = User.objects.get(id=user_id)
        token_serializer = UserSerializer(user)

        response = {
            "user_id": user_id,
            "account_num": token_serializer.data['id']
        }
        return Response(token_serializer.data, status=status.HTTP_200_OK)
        

@api_view(['GET'])
@permission_classes([AllowAny])
@authentication_classes([JSONWebTokenAuthentication])
def user_list(request, pk):
    if request.method == 'GET':
        users = User.objects.get(pk=pk)
        user_serializers = UserSerializer(users)
        return Response(user_serializers.data)
