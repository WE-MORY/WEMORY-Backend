from django.shortcuts import render
from django.http import HttpResponse

import requests
import json

def getCellCerti(request):
    url = 'https://openapi.wooribank.com:444/oai/wb/v1/login/getCellCerti'
    headers = {'appkey': 'l7xxqenvTsl9kgFUTcSCdoNBDsgq2zMyFCZA', 'Content-Type': 'application/json'}
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