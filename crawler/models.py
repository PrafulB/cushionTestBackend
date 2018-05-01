from django.db import models

class HitStats(models.Model):
    """ Class To Track Stats of Hits Received """
    userIP = models.CharField(max_length=255, blank=False, unique=False)
    requestTimestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        """ Return a more readable string for the data contained """
        return self.userIP + " " + str(self.requestTimestamp)