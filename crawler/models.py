from django.db import models

class HitStats(models.Model):
    """ Class To Track Stats of Hits Received """
    api = models.CharField(max_length=255, blank=False, unique=False)
    userIP = models.CharField(max_length=255, blank=False, unique=False)
    requestTimestamp = models.DateTimeField(auto_now=True)