import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from crawler.crawler import Crawler

# Max number of most frequent words to be returned
NUM_WORDS = 10

def index(request) :
    return Response("YOU DID IT!")

@api_view(['POST'])
@parser_classes((JSONParser,))
def getURLData(request) :
    """
    API Handler for Getting the URL and returning the Scraped Text &
    Most Frequently Occurring Words
    """
    if request.method == "POST" :
        
        textContents = Crawler.getText(request.data["url"])
        frequentWords = Crawler.getMostFrequentWords(textContents, NUM_WORDS)

        frequentWordsDict = [{"word": word[0], "freq": word[1]} for word in frequentWords]
        
        return Response({
            'text' : textContents,
            'wordFreqs': frequentWordsDict
        })
        