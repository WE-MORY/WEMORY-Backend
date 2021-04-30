from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import AccountSerializer
from .models import Account
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status

@api_view(['GET','POST'])
@permission_classes([AllowAny])
def account_list(request):
    if request.method == "POST":
        serializers=AccountSerializer(data=request.data)
        if serializers.is_valid(raise_exception=True):
            serializers.save()
            return Response(serializers.data)
    else:
        diaries = Account.objects.all()
        serializers = AccountSerializer(diaries, many=True)
        return Response(serializers.data)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([AllowAny])
def account_detail(request, pk):
    try: 
        account = Account.objects.get(pk=pk) 
    except Account.DoesNotExist: 
        return JsonResponse({'message': 'The account does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        account_serializer = AccountSerializer(account) 
        return Response(account_serializer.data) 
 
    elif request.method == 'PUT': 
        account_data = JSONParser().parse(request) 
        account_serializer = AccountSerializer(account, data=account_data) 
        if account_serializer.is_valid(): 
            account_serializer.save() 
            return JsonResponse(account_serializer.data) 
        return JsonResponse(account_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        account.delete() 
        return JsonResponse({'message': 'account was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    