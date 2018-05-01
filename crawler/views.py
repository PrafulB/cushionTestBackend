import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from crawler.crawler import Crawler

# Create your views here.

def index(request) :
    return Response("YOU DID IT!")

@api_view(['POST'])
@parser_classes((JSONParser,))
def getURLData(request) :
    if request.method == "POST" :
        textContents = Crawler.getText(request.data["url"])
        frequentWords = Crawler.getMostFrequentWords(textContents)
        return Response({
            'data': "waitForIt"
        })
        