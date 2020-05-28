from django.db import models
from django.contrib.auth.models import User
import string, secrets

# Create your models here.


def generateShortUrl(linklength=5):

    return ''.join(secrets.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for i in range(linklength)) 


class Link(models.Model):
    shorturl = models.CharField(max_length=100, null=True, blank=True)
    longurl = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.PROTECT, blank=True, null=True)

    def __str__(self):
        return self.shorturl
    
    def save(self, *args, **kwargs):
        
        shortURL = generateShortUrl()

        while(Link.objects.filter(shorturl=shortURL).exists()):
            shortURL = generateShortUrl()

        self.shorturl = generateShortUrl()

        super().save(*args, **kwargs)


    