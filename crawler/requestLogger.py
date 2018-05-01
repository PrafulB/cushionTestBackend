from crawler.models import HitStats
from django.utils import timezone

class RequestLoggingMiddleware:
    """ Class to log all received requests and add to DB """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        """
        Function that logs the userIP and the timestamp to the db
        """
        req = HitStats(userIP=request.get_host(), requestTimestamp=timezone.now())
        req.save()
        response = self.get_response(request)
        return response