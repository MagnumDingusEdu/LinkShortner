from django.db import models
from django.contrib.auth.models import User
import string, secrets

# Create your models here.


def generateShortUrl(linklength=5):

    shortURL =  ''.join(secrets.choice(string.digits + string.ascii_lowercase) for i in range(linklength)) 


    

    while(Link.objects.filter(shorturl=shortURL).exists()):
        shortURL = ''.join(secrets.choice(string.digits + string.ascii_lowercase) for i in range(linklength))

    return shortURL

    super().save(*args, **kwargs)
class Link(models.Model):
    shorturl = models.CharField(max_length=100, null=True, blank=True, default=generateShortUrl)
    longurl = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)
    clickcount = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.shorturl
    



