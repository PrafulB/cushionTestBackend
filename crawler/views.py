from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def index(request) :
    return HttpResponse("YOU DID IT!")

@api_view(['POST'])
def getURLData(request) :
    if request.method == "POST" :
        print(request.data)