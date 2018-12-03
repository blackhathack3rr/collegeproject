from django.shortcuts import render


import requests
# Create your views here.
API = "https://api.coinmarketcap.com/v1/ticker/?limit=10"



def get_crypto(request):
    data = requests.get(API).json()
    ctx={
        "data":data
    }
    return render(request,template_name="crypto_currency.html",context=ctx)


