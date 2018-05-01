from django.test import TestCase
from django.utils import timezone
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from .models import HitStats
import json

class ModelTest(TestCase):
    """ Class To Define Test Cases for the Crawler Model """

    def setUp(self):
        self.HitStats_userIP = "1.1.1.1"
        self.HitStats_timestamp = timezone.now()
        self.HitStatsInstance = HitStats(userIP=self.HitStats_userIP, requestTimestamp=self.HitStats_timestamp)

    def testToCreateSampleRequestLog(self):
        requestCountBefore = HitStats.objects.count()
        self.HitStatsInstance.save()
        requestCountAfter = HitStats.objects.count()
        self.assertNotEqual(requestCountBefore, requestCountAfter)



class ViewTest(TestCase):
    """ Class To Define Test Cases for the Crawler View 
    TODO: 
    1. Assert That Response Content is also equal on good and bad URLs instead of just the status codes.
    2. Define Test Cases for URLs and pages containing non-UTF-8 strings.
    3. Define more tests
    """

    def setUp(self):
        self.client = APIClient()
        self.safeURL = {
            "url": "https://raw.githubusercontent.com/tidwall/sjson/master/LICENSE" 
        }
        self.badURL = {
            "url": "abcd" 
        }
        
        # self.safeResponse = json.dumps({"wordFreqs":[{"freq":14,"word":"THE"},{"freq":8,"word":"OR"},{"freq":8,"word":"OF"},{"freq":8,"word":"TO"},{"freq":6,"word":"IN"},{"freq":5,"word":"SOFTWARE"},{"freq":4,"word":"AND"},{"freq":3,"word":"ANY"},{"freq":3,"word":"COPYRIGHT"},{"freq":3,"word":"IS"}],"text":"The MIT License (MIT)\n\nCopyright (c) 2016 Josh Baker\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of\nthis software and associated documentation files (the \"Software\"), to deal in\nthe Software without restriction, including without limitation the rights to\nuse, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of\nthe Software, and to permit persons to whom the Software is furnished to do so,\nsubject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS\nFOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR\nCOPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER\nIN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN\nCONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.\n\n"})
        # self.unsafeResponse = json.dumps({"error":"Malformed URL"})

    
    def testForGoodURL(self):
        response = self.client.post(
            reverse('getURLData'),
            self.safeURL,
            format="json")
        # self.maxDiff=None
        # self.assertJSONEqual(response.content.decode('utf8').replace("'", '"'), self.safeResponse)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

   
    def testForBadURL(self):
        response = self.client.post(
            reverse('getURLData'),
            self.badURL,
            format="json")
        
        # self.assertJSONEqual(response.content.decode('utf8').replace("'", '"'), self.unsafeResponse)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)



class LoggerTest(TestCase):
    """ Class to test if the middleware logs each request and adds it to the db. """

    def setUp(self):
        self.client = APIClient()
        self.URL = {
            "url": "https://raw.githubusercontent.com/tidwall/sjson/master/LICENSE" 
        }
    
    def testIfRequestIsLogged(self):
        requestsLoggedCountBefore = HitStats.objects.count()
        
        _ = self.client.post(
            reverse('getURLData'),
            self.URL,
            format="json")
        
        requestsLoggedCountAfter = HitStats.objects.count()

        self.assertNotEqual(requestsLoggedCountBefore, requestsLoggedCountAfter)