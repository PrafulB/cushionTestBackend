import datetime

class RequestLoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(request.get_host(), datetime.datetime.now().isoformat())
        response = self.get_response(request)
        return response