import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from crawler.crawler import Crawler
from .models import HitStats

# Max number of most frequent words to be returned
NUM_WORDS = 10

class CrawlerView:
    """ Class To Implement the API Handler for the Page Scraper """

    @staticmethod
    @api_view(['POST'])
    @parser_classes((JSONParser,))
    def getURLData(request, format=None) :
        """
        API Handler for Getting the URL and returning the Scraped Text &
        Most Frequently Occurring Words
        """
        if request.method == "POST" :
            
            textContents = Crawler.getText(request.data["url"])
            # If no contents received, assume that the URL is problematic.
            if textContents == "" :
                return Response(data={
                    "error" : "Malformed or Inaccessible URL"
                }, status=status.HTTP_400_BAD_REQUEST)

            frequentWords = Crawler.getMostFrequentWords(textContents, NUM_WORDS)

            #Convert the list of words into a dictionary, making it more easily readable by the front-end.
            frequentWordsDict = [{"word" : word[0], "freq" : word[1]} for word in frequentWords]
            
            return Response(data={
                "text" : textContents,
                "wordFreqs": frequentWordsDict
            }, status=status.HTTP_200_OK)
            