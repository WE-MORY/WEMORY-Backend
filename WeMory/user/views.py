from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

from .serializers import UserCreateSerializer
from .models import User

from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

headers = {'appkey': 'l7xxqenvTsl9kgFUTcSCdoNBDsgq2zMyFCZA', 'Content-Type': 'application/json'}

def getCellCerti(request):
    url = 'https://openapi.wooribank.com:444/oai/wb/v1/login/getCellCerti'
    data = {
        "dataHeader": {
            "UTZPE_CNCT_IPAD": "",
            "UTZPE_CNCT_MCHR_UNQ_ID": "",
            "UTZPE_CNCT_TEL_NO_TXT": "",
            "UTZPE_CNCT_MCHR_IDF_SRNO": "",
            "UTZ_MCHR_OS_DSCD": "",
            "UTZ_MCHR_OS_VER_NM": "",
            "UTZ_MCHR_MDL_NM": "",
            "UTZ_MCHR_APP_VER_NM": ""
        },
        "dataBody": {
            "COMC_DIS": "1",
            "HP_NO": "01012345678",
            "HP_CRTF_AGR_YN": "Y",
            "FNM": "홍길동",
            "RRNO_BFNB": "930216",
            "ENCY_RRNO_LSNM": "1234567"
        }
    }

    response = requests.post(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    return HttpResponse(response)

def executeCellCerti(request):
    url = 'https://openapi.wooribank.com:444/oai/wb/v1/login/executeCellCerti'
    data = {
        "dataHeader": {
            "UTZPE_CNCT_IPAD": "",
            "UTZPE_CNCT_MCHR_UNQ_ID": "",
            "UTZPE_CNCT_TEL_NO_TXT": "",
            "UTZPE_CNCT_MCHR_IDF_SRNO": "",
            "UTZ_MCHR_OS_DSCD": "",
            "UTZ_MCHR_OS_VER_NM": "",
            "UTZ_MCHR_MDL_NM": "",
            "UTZ_MCHR_APP_VER_NM": ""
        },
        "dataBody": {
            "RRNO_BFNB": "930216",
            "ENCY_RRNO_LSNM": "1234567",
            "ENCY_SMS_CRTF_NO": "1111111",
            "CRTF_UNQ_NO": "MG12345678901234567890"
        }
    }
    response = requests.post(url, data=json.dumps(data).encode('utf-8'), headers=headers)
    return HttpResponse(response)

@api_view(['POST'])
@permission_classes([AllowAny])
def createUser(request):
    if request.method == 'POST':
        serializer = UserCreateSerializer(data=request.data)
        if not serializer.is_valid(raise_exception=True):
            return Response({"message": "Body 값이 잘못되었습니다."}, status=status.HTTP_409_CONFLICT)
        
        if User.objects.filter(email=serializer.validated_data['email']).first() is None:
            serializer.save()
            return Response({"message": "ok"}, status=status.HTTP_201_CREATED)
        return Response({"message": "중복된 이메일입니다."}, status=status.HTTP_409_CONFLICT)